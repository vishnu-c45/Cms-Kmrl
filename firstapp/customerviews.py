from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Count

import datetime
import json
from django.utils import timezone
from django.db.models import Sum
from .models import *
from .serializers import AdminSerializer, NotificationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from datetime import datetime,timedelta 
from django.db.models.signals import post_save
from django.dispatch import receiver
from num2words import num2words
from django.core.files.storage import FileSystemStorage
import razorpay
from django.conf import settings
from django.core.mail import send_mail
# import requests


def customer_dasboard(request):
    if 'lid' in request.session:
        Id=request.session['lid']
        login=login_table.objects.get(id=Id)
        customer=Customer_contact.objects.get(id=login.customer_id)
        recent_invoices=Invoices.objects.filter(customer_contact_id=customer.id,status__in=['2','3','4']).order_by('-id')[:5]
        recent_payments=Payments_Data.objects.filter(customer_id=customer.id).order_by('-id')[:5]
        invoicesum = Invoices.objects.filter(customer_contact_id=customer.id,status__in=['2','3','4']).count()
        invoicepaid = Invoices.objects.filter(customer_contact_id=customer.id,status__in=['3']).count()
        invoicepending = Invoices.objects.filter(customer_contact_id=customer.id,status__in=['2','4']).count()
        paymentsum = Payments_Data.objects.filter(customer_id=customer.id,status__in=['1','2']).count()
        payments = Payments_Data.objects.filter(customer_id=customer.id,status=1).count()
        pending = Payments_Data.objects.filter(customer_id=customer.id,status=2).count()
        from_date= ''
        to_date= ''
        if request.method == 'POST':
            from_date = request.POST.get('fromDate')
            to_date = request.POST.get('toDate')
            if from_date and to_date:
                from_datetime = datetime.strptime(from_date, '%Y-%m-%d')
                to_datetime = datetime.strptime(to_date, '%Y-%m-%d')
                to_datetime += timedelta(days=1)
                invoicesum = Invoices.objects.filter(customer_contact_id=customer.id,status__in=['2','3','4'],created_on__range=(from_datetime, to_datetime)).count()
                invoicepaid = Invoices.objects.filter(customer_contact_id=customer.id,status__in=['3'],created_on__range=(from_datetime, to_datetime)).count()
                invoicepending = Invoices.objects.filter(customer_contact_id=customer.id,status__in=['2','4'],created_on__range=(from_datetime, to_datetime)).count()
                paymentsum = Payments_Data.objects.filter(customer_id=customer.id,status__in=['1','2'],created_on__range=(from_datetime, to_datetime)).count()
                payments = Payments_Data.objects.filter(customer_id=customer.id,status=1,created_on__range=(from_datetime, to_datetime)).count()
                pending = Payments_Data.objects.filter(customer_id=customer.id,status=2,created_on__range=(from_datetime, to_datetime)).count()
        return render(request,'customer_dasboard.html',{'recent_invoices':recent_invoices,'recent_payments':recent_payments,'invoicesum':invoicesum,'invoicepaid':invoicepaid,'invoicepending':invoicepending,'paymentsum':paymentsum,'payments':payments,'pending':pending,'fromdate': from_date,'todate': to_date,})
    else:
        return redirect('user_logout')

def due_notification(request):
    if 'lid' in request.session:
        Id=request.session['lid']
        login=login_table.objects.get(id=Id)
        current_date = timezone.now().date()
        customernoti=login_table.objects.get(customer_id=login.customer_id)

        # Get invoices approaching or due in 1, 3, and 5 days
        approaching_invoices = Invoices.objects.filter(
            status=2,customer_contact_id=login.customer_id,
            due_date__gte=current_date,
            due_date__lte=current_date + timedelta(days=5),
        )

        for invoice in approaching_invoices:
            due_date_diff = invoice.due_date - current_date
            days_until_due = due_date_diff.days

            if days_until_due == 5:
                color = "bg-success"  
            elif days_until_due == 3:
                color = "bg-warning"  
            elif days_until_due == 1:
                color = "bg-danger"  
            else:
                color = ""

             # Send notification only for invoices with color assigned
            if color:
                notification, created = Notification.objects.get_or_create(
                    invoice_no=invoice.invoice_no,
                    color=color,
                    defaults={
                        'message': f"Invoice #{invoice.invoice_no} with due date {invoice.due_date} is approaching.",
                        'status': 1,
                        'type': 5,
                    }
                )
                if created:
                    customernoti.notifications.add(notification)
                    subject = 'Invoice Due Reminder'
                    message = f'Hello {customernoti.login_name},\n\nThis is an urgent reminder that your invoice is due for payment.\n\nInvoice Details:\n\nInvoice Number: {invoice.invoice_no}\nAmount Due: Rs.{invoice.total_amount}\nDue Date: {invoice.due_date}\n\nPlease make the payment as soon as possible to avoid any late payment charges. If you have already made the payment, kindly disregard this reminder.\n\nThank you for your prompt attention to this matter.\n\nBest regards,\nThe KMRL Team'
                    from_email = settings.EMAIL_HOST_USER
                    to_email = customernoti.email
                    send_mail(subject, message, from_email, [to_email])
        return HttpResponse('true')            


def register(request):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'POST':
        customer_name = request.POST['customername']
        email = request.POST['email']
        phone_number = request.POST['phone']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        username = request.POST['username']

        user = login_table.objects.filter(username__iexact=username)
        user1 = Customer_contact.objects.filter(username__iexact=username, status__in=['1', '2', '3', '5'])

        if user.exists() or user1.exists():
            return HttpResponse('exists')
        else:
            if password == cpassword:
                hashpassword = make_password(password)
                std = Customer(
                    customer_name=customer_name,
                    created_on=date,
                    status=2
                )
                std.save()
                std2 = Customer_contact(
                    customer_id=std.id,
                    password=hashpassword,
                    username=username,
                    email=email,
                    phone_number=phone_number,
                    created_on=date,
                    status=3,
                )
                std2.save()
                # Send notification to admin
                admins = login_table.objects.filter(usertype=1)  
                message = f"New customer registered: {customer_name}"
                for admin in admins:
                    notification = Notification.objects.create(message=message, status=1, type=1)
                    admin.notifications.add(notification)
                return HttpResponse('true')
            else:
                return HttpResponse('false')
    return render(request, 'register.html')

def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        customer_name = request.POST.get('customerName')
        types = request.POST.get('type')
        area = request.POST.get('Area')
        loc = request.POST.get('station')
        subject=''
        
        # Send email to the registered customer
        if types == "1":
            subject = 'Registration Successful'
            message = f'Dear {customer_name},\n\nThank you for registering with our website. We are pleased to inform you that your registration has been successfully completed. \n\nPlease feel free to explore our website and take advantage of all the features and services we offer. If you have any questions or need assistance, our support team is ready to help.\n\nBest regards,\nThe KMRL Team'
            from_email = settings.EMAIL_HOST_USER
            to_email = email
            send_mail(subject, message, from_email, [to_email])

        elif types == "2":
            customers= login_table.objects.filter(usertype=2,status=1)
            subject = 'Rental Space Available'
            from_email = settings.EMAIL_HOST_USER
            for p in customers:
                message = f'Hello {p.login_name},\n\nWe are excited to inform you that a new rental space is now available for you.\n\nDetails of the space:\n\nSpace Name: {email}\nArea: {area}sqft\nLocation: {loc}\n\n If you are interested or have any questions, please feel free to contact us.\n\nThank you for being a valued customer.\n\nBest regards,\nThe KMRL Team'
                to_email = p.email
                send_mail(subject, message, from_email, [to_email])

        elif types == "3":
            customers= login_table.objects.get(customer_id=customer_name)
            subject = 'Invoice Generated'
            message = f'Hello {customers.login_name},\n\nThis mail is to inform you that a new invoice has been generated for your rental space.\n\nInvoice Details:\n\nInvoice Number: {email}\nAmount: {area}\nDue Date: {loc}\n\nPlease review the invoice and make the payment by the due date. If you have any questions or concerns regarding the invoice, feel free to reach out to our support team.\n\nThank you for your continued business.\n\nBest regards,\nThe KMRL Team'
            from_email = settings.EMAIL_HOST_USER
            to_email = customers.email
            send_mail(subject, message, from_email, [to_email])

        elif types == "4":
            subject = 'Invoice Generated'
            from_email = settings.EMAIL_HOST_USER
            customers= Invoices.objects.filter(status=2)
            for p in customers:
                message = f'Hello {p.customer_contact.customer.customer_name},\n\nThis mail is to inform you that a new invoice has been generated for your rental space.\n\nInvoice Details:\n\nInvoice Number: {p.invoice_no}\nAmount: {p.total_amount}\nDue Date: {p.due_date}\n\nPlease review the invoice and make the payment by the due date. If you have any questions or concerns regarding the invoice, feel free to reach out to our support team.\n\nThank you for your continued business.\n\nBest regards,\nThe KMRL Team'
                to_email = p.customer_contact.email
                send_mail(subject, message, from_email, [to_email])

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

def Customer_invoice(request):
    if 'lid' in request.session:
        Id=request.session['lid']
        login=login_table.objects.get(id=Id)
        customer=Customer_contact.objects.get(id=login.customer_id)
        std = Invoices.objects.filter(customer_contact_id=customer.id,status__in=['2','3','4']).order_by('-id')
        paid = Invoices.objects.filter(customer_contact_id=customer.id,status=3).order_by('-id')
        pending = Invoices.objects.filter(customer_contact_id=customer.id,status=2).order_by('-id')
        overdue = Invoices.objects.filter(customer_contact_id=customer.id,status=4).order_by('-id')
        return render(request, 'customer_invoices.html', {'std': std,'paid':paid,'pending':pending,'overdue':overdue})
    return redirect('loginfunc')

def Customer_invoice_details(request, pk):
    if 'lid' in request.session:
        std = Invoices.objects.get(id=pk)
        contract = Contract.objects.get(master_space_id=std.master_space_id,status=1)
        spaces = Space.objects.filter(master_space_id=std.master_space_id)
        spaces_count = Space.objects.filter(master_space_id=std.master_space_id).count()
        number = std.total_amount
        number_in_words = num2words(number, lang='en').title()
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create(
            {"amount": int(std.total_amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        return render(request, 'customer_invoice_details.html', {'std': std, 'contract': contract, 'spaces': spaces,'spaces_count':spaces_count, 'number_in_words': number_in_words,'payment':payment})
    return redirect('loginfunc')

def Customer_profile(request):
    if 'lid' in request.session:
        Id=request.session['lid']
        std=login_table.objects.get(id=Id)
        customer=Customer_contact.objects.get(id=std.customer_id)
        return render(request, 'customer_profile.html',{'std':std,'customer':customer})
    return redirect('loginfunc')

def Customer_edit_profile(request):
    if 'lid' in request.session:
        login_id=request.session['lid']
        std=login_table.objects.get(id=login_id)
        customer=Customer_contact.objects.get(id=std.customer_id)
        customer_main=Customer.objects.get(id=customer.customer_id)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if request.method == 'POST':
            std=login_table.objects.get(id=login_id)
            customer=Customer_contact.objects.get(id=std.customer_id)
            customer_main=Customer.objects.get(id=customer.customer_id)
            std.login_name = request.POST['name']
            customer_main.customer_name = request.POST['name']
            std.email =request.POST['email']
            customer.email = request.POST['email']
            std.phno = request.POST['phone']
            customer.phone_number = request.POST['phone']
            # Check if the username field is being updated
            if std.username != request.POST['username']:
                std.username = request.POST['username']
                customer.username = request.POST['username']
                # Perform the existence check only for username updates
                user = login_table.objects.filter(username__iexact=std.username)
                if user.exists():
                    return HttpResponse('exists')
            customer.city = request.POST['city']
            customer.district = request.POST['district']
            customer.pincode = request.POST['pincode']
            customer.address = request.POST['address']
            customer.gst_no = request.POST['gst_no']
            customer.pan_no = request.POST['pan_no']
            customer.state_code = request.POST['state_code']
            customer.state = request.POST['state']
            customer_main.business_type = request.POST['business_type']
            customer_main.business_name = request.POST['business_name']
            std.updated_on = date
            std.updated_by = login_id
            if 'pic' in request.FILES:
                profile_pic = request.FILES['pic']
                fs = FileSystemStorage(location='media/')
                filename = 'profilepicture.jpg'
                saved_file = fs.save(filename, profile_pic)
                url = fs.url(saved_file)
            else:
                url= std.profile_pic    
            std.profile_pic = url
            std.save()
            customer.save()
            customer_main.save()
            return HttpResponse('true')

        std=login_table.objects.get(id=login_id)
        customer=Customer_contact.objects.get(id=std.customer_id)
        
        return render(request, 'edit_customer_profile.html',{'std':std,'customer':customer})
    return redirect('loginfunc')

@api_view(['GET'])
def view_profile(request):
    if 'lid' in request.session:
        login_id = request.session['lid']
        user= login_table.objects.get(id=login_id)
        my_serializer = AdminSerializer(user)
        return Response(my_serializer.data)

def Customer_change_password(request):
    if 'lid' in request.session:
        if request.method == "POST":
            current_password = request.POST['current_password']
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']
            Id=request.session['lid']
            std=login_table.objects.get(id=Id)
            matchpassword = check_password(current_password,std.password)
            if matchpassword:
                    hashpassword = make_password(new_password)
                    std.password = hashpassword
                    std.save()
                    return HttpResponse('true')
            else:
                return HttpResponse('false')
        return render(request, 'customer_change_password.html')
    return redirect('loginfunc') 


def invoice_payment(request):
    if 'lid' in request.session:
        if request.method == "POST":
            id=request.session['lid']
            login_id=login_table.objects.get(id=id)
            payment_id = request.POST.get("razorpay_payment_id")
            order_id = request.POST.get("razorpay_order_id")
            signature = request.POST.get("razorpay_signature")
            amount = request.POST.get("PaymentAmount")
            phno =request.POST.get('MobileNumber')
            invoiceid =request.POST.get('InvoiceID')
            customerid =request.POST.get('CustomerID')
            spaceid =request.POST.get('Space_ID')
            amount=int(amount)/100
            date = datetime.now().strftime('%Y-%m-%d')
            std=Payments_Data(customer_id=customerid,
                              invoice_id=invoiceid,
                              master_space_id=spaceid,
                              transaction_id=payment_id,
                              payment_order_id=order_id,
                              payment_signature=signature,
                              payment_amount=amount,
                              created_on=date,
                              created_by=login_id,
                              status=1)
            std.save()
            Invoices.objects.filter(id=invoiceid).update(status=3)
            invoice=Invoices.objects.get(id=invoiceid)
            admins = login_table.objects.filter(usertype=1) 
            profile= None
            if login_id.profile_pic:
                profile = f"{login_id.profile_pic}"
            name = f"{login_id.login_name} "
            invoices = f" #{invoice.invoice_no}"

            for admin in admins:
                notification = Notification.objects.create(name=name,invoice_no=invoices,profile_pic=profile,status=1,type=3)
                admin.notifications.add(notification)
            return HttpResponse('true')
    return redirect('loginfunc') 
        
        
def customer_payments(request):
    if 'lid' in request.session:
        login_id= request.session['lid']
        login=login_table.objects.get(id=login_id)
        payments=Payments_Data.objects.filter(customer_id=login.customer_id,status__in=['1','2','3'])
        paid=Payments_Data.objects.filter(customer_id=login.customer_id,status=1)
        pending=Payments_Data.objects.filter(customer_id=login.customer_id,status=2)
        declined=Payments_Data.objects.filter(customer_id=login.customer_id,status=3)
        payment_count=Payments_Data.objects.filter(customer_id=login.customer_id).count()
        payment_paid=Payments_Data.objects.filter(customer_id=login.customer_id,status=1).count()
        payment_pending=Payments_Data.objects.filter(customer_id=login.customer_id,status=2).count()
        payment_declined=Payments_Data.objects.filter(customer_id=login.customer_id,status=3).count()
        return render(request,'customer_payments.html',{'payments':payments,'payment_count':payment_count,'payment_paid':payment_paid,'payment_pending':payment_pending,'payment_declined':payment_declined,'paid':paid,'pending':pending,'declined':declined})
    return redirect('loginfunc') 

def customer_contract(request):
    if 'lid' in request.session:
        login_id= request.session['lid']
        login=login_table.objects.get(id=login_id)
        std = Contract.objects.filter(customer_contact_id=login.customer_id,status=1).order_by('-id')
        spaces=Space.objects.filter(status=1)
        contractcount = Contract.objects.filter(customer_contact_id=login.customer_id,status=1).count()
        depositcount = Contract.objects.filter(
            customer_contact_id=login.customer_id,status=1).aggregate(TOTAL=Sum('security_deposit'))['TOTAL']
        rent = Contract.objects.filter(
           customer_contact_id=login.customer_id,status=1).aggregate(TOTAL=Sum('rent_amount'))['TOTAL']
        if depositcount ==None:
            depositcount=0
        if rent ==None:
            rent=0
        current_date = timezone.now().date()
        # Update the status of contract in bulk
        Contract.objects.filter(customer_contact_id=login.customer_id,status=1, tenure_end_date__lt=current_date).update(status=2)

        return render(request, 'view_customer_contract.html', {'std': std, 'contractcount': contractcount, 'depositcount': depositcount, 'rent': rent,'spaces':spaces})
    return redirect('loginfunc')


def customer_contract_details(request,pk):
    if 'lid' in request.session:
        std = Contract.objects.get(id=pk)
        spaces = Space.objects.filter(master_space_id=std.master_space_id)
        customer = Customer_contact.objects.get(id=std.customer_contact_id)
        try:
            user_update = login_table.objects.get(id=std.updated_by)
        except login_table.DoesNotExist:
            user_update = ''
        context = {
            'std': std,
            'updated': user_update, 'spaces': spaces, 'customer': customer

        }
        return render(request, 'customer_contract_details.html', context)
    return redirect('loginfunc')

def vacantSpaces(request):
    if 'lid' in request.session:
        std = Space.objects.filter(status=1,vacancy_status=1).order_by('-id')
        metro = MetroStationContact.objects.filter(status=1)
        spaces = Space.objects.filter(status=1).values('area_level').annotate(count=Count('area_level')).distinct()
        space_type = Space.objects.filter(status=1).values('space_type').annotate(count=Count('space_type')).distinct()
        vac_count = Space.objects.filter(status=1, vacancy_status=1,space_type='Office').count()
        occ_count = Space.objects.filter(status=1, vacancy_status=1,space_type="Kiosk").count()
        space_count = Space.objects.filter(status=1, vacancy_status=1).count()
        return render(request,'vacantSpaces.html',{'std': std, 'vac': vac_count, 'occ': occ_count, 'space': space_count, 'metro': metro, 'spaces': spaces, 'space_type': space_type})
    return redirect('loginfunc')


def View_Vacant_space_details(request, pk):
    if 'lid' in request.session:
        std = Space.objects.get(id=pk)
        login_id=request.session['lid']
        contract = Contract.objects.filter(master_space_id=pk, status__in=['1', '2']).count()
        invoice = Invoices.objects.filter(master_space_id=pk).count()
        user_created = login_table.objects.get(id=std.created_by_id)
        payment_count = Payments_Data.objects.filter(master_space_id=pk).count()
        try:
            intrestSpace =IntrestSpace.objects.get(space_id=pk,login_id=login_id)
        except IntrestSpace.DoesNotExist:
            intrestSpace = ''
        try:
            user_update = login_table.objects.get(id=std.updated_by)
        except login_table.DoesNotExist:
            user_update = ''
        print('intrestspace',intrestSpace)
        return render(request, 'view_Vacant_spacedetails.html', {'std': std, 'created': user_created, 'updated': user_update, 'contract_count': contract, 'invoice_count': invoice, 'payment_count': payment_count,'intrestspace':intrestSpace})
    return redirect('loginfunc')

#Notification Api
class CNotificationAPIView(APIView):
    def get(self, request):
        if 'lid' in request.session:
            login_id = request.session['lid']
            user = login_table.objects.get(id=login_id)
            notifications = user.notifications.filter(status=1).order_by('-id')
            serializer = NotificationSerializer(notifications, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Not logged in.'})

    def post(self, request):
        if 'lid' in request.session:
            login_id = request.session['lid']
            user = login_table.objects.get(id=login_id)
            notifications = user.notifications.filter(status=1)

            for p in notifications:
                p.status = 2
                p.save()
            return HttpResponse('Notifications cleared successfully')
        
@api_view(['POST'])
def intestSpace(request):
    if 'lid' in request.session:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        login_id = request.session['lid']
        user= login_table.objects.get(id=login_id)
        space=request.POST['spaceId']
        interstSpace=IntrestSpace.objects.filter(login_id=login_id,space_id=space)
        if interstSpace.exists():
             return Response('false')
        else :
            print("space_id",space,date)
            std =IntrestSpace(login_id=user,
                            space_id_id=space,
                            created_on=date)
            std.save()
            return Response('true')