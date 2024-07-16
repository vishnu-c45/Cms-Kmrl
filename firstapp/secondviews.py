from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
import datetime
from django.utils import timezone
from .models import *
from .views import *
from .serializers import SpaceModelSerializer, BankSerializer, GrievanceSerializer, AdminSerializer, GenralParameterSerializer
from num2words import num2words
from django.conf import settings
import os
from django.shortcuts import render
from django.db.models import Count
from django.db.models import Max
from django.db.models import Q
from calendar import monthrange
import razorpay
from django.conf import settings
from django.core.mail import send_mail
# import requests

def Viewspaces(request):
    if 'supid' in request.session:
        std = Space.objects.filter(status=1).order_by('-id')
        metro = MetroStationContact.objects.filter(status=1)
        spaces = Space.objects.filter(status=1).values('area_level').annotate(count=Count('area_level')).distinct()
        space_type = Space.objects.filter(status=1).values('space_type').annotate(count=Count('space_type')).distinct()
        vac_count = Space.objects.filter(status=1, vacancy_status=1).count()
        occ_count = Space.objects.filter(status=1, vacancy_status=2).count()
        space_count = Space.objects.filter(status=1).count()
        return render(request, 'viewspaces.html', {'std': std, 'vac': vac_count, 'occ': occ_count, 'space': space_count, 'metro': metro, 'spaces': spaces, 'space_type': space_type})
    return redirect('loginfunc')

def Addspaces(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        metro = MetroStationContact.objects.filter(status=1)
        space_type=General_parameter.objects.filter(gp_type='space_type',status=1)
        area_level=General_parameter.objects.filter(gp_type='area_level',status=1)
        area_type=General_parameter.objects.filter(gp_type='area_type',status=1)
        area_side=General_parameter.objects.filter(gp_type='area_side',status=1)
        context ={'metro': metro,'space_type':space_type,'area_level':area_level,'area_type':area_type,'area_side':area_side}
        if request.method == 'POST':
            stationname = request.POST['stationname']
            spacename = request.POST['spacename']
            spacetype = request.POST['spacetype']
            areatype = request.POST['areatype']
            areaside = request.POST['areaside']
            arealevel = request.POST['arealevel']
            area = request.POST['area']
            std = Space(metrostation_id=stationname,
                        space_name=spacename,
                        space_type=spacetype,
                        area_type=areatype,
                        area_side=areaside,
                        area_level=arealevel,
                        area=area,
                        created_on=date,
                        created_by_id=login_id,
                        vacancy_status=1,
                        status=1)
            std.save()
            master = Space.objects.get(id=std.id)
            master.master_space_id = std.id
            master.save()
            customers = login_table.objects.filter(usertype=2) 
            message = f"{spacename} is available now"
            for admin in customers:
                notification = Notification.objects.create(message=message,status=1,type=6)
                admin.notifications.add(notification)
            return HttpResponse('Succesfully Inserted')
        return render(request, 'add_spaces.html',context)
    return redirect('loginfunc')

def View_space_details(request, pk):
    if 'supid' in request.session:
        std = Space.objects.get(id=pk)
        contract = Contract.objects.filter(master_space_id=pk, status__in=['1', '2']).count()
        invoice = Invoices.objects.filter(master_space_id=pk).count()
        user_created = login_table.objects.get(id=std.created_by_id)
        payment_count = Payments_Data.objects.filter(master_space_id=pk).count()
        try:
            user_update = login_table.objects.get(id=std.updated_by)
        except login_table.DoesNotExist:
            user_update = ''
        return render(request, 'viewspacedetails.html', {'std': std, 'created': user_created, 'updated': user_update, 'contract_count': contract, 'invoice_count': invoice, 'payment_count': payment_count})
    return redirect('loginfunc')

def Update_space(request, pk):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        metro = MetroStationContact.objects.filter(status=1)
        space = Space.objects.filter(status=1)
        if request.method == 'POST':
            std = Space.objects.get(id=pk)
            std.metrostation_id = request.POST['stationname']
            std.space_name = request.POST['spacename']
            std.space_type = request.POST['spacetype']
            std.area_type = request.POST['areatype']
            std.area_side = request.POST['areaside']
            std.master_space_id = request.POST['masterspace']
            std.area_level = request.POST['arealevel']
            std.area = request.POST['area']
            std.updated_on = date
            std.updated_by = login_id
            std.save()
            return HttpResponse("Updated Successfully")
        std = Space.objects.get(id=pk)
        return render(request, 'update_spaces.html', {'std': std, 'metro': metro, 'master': space})
    return redirect('loginfunc')

def deletespace(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Space.objects.get(id=pk)
            std.vacancy_status = 3
            std.save()
            return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')

def activatespace(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Space.objects.get(id=pk)
            std.vacancy_status = 1
            std.save()
            customers = login_table.objects.filter(usertype=2) 
            message = f"{std.space_name} is available now"
            for admin in customers:
                notification = Notification.objects.create(message=message,status=1,type=6)
                admin.notifications.add(notification)
            return HttpResponse("Activated")
    return redirect('loginfunc')

def Viewcustomers(request):
    if 'supid' in request.session:
        std = Customer_contact.objects.prefetch_related('invoices', 'payments_data').filter(status__in=['1', '2', '3', '5']).order_by('-id')
        customercount = Customer_contact.objects.filter(status__in=['1', '2', '3', '5']).count()
        payments = Payments_Data.objects.filter(status=1).aggregate(TOTAL=Sum('payment_amount'))['TOTAL']
        invoice_count = Invoices.objects.all().count()
        due = Invoices.objects.filter(status__in=['2', '4']).aggregate(TOTAL=Sum('total_amount'))['TOTAL']
        depositcount = Contract.objects.filter(
            status=1).aggregate(TOTAL=Sum('security_deposit'))['TOTAL']
        app = Customer_contact.objects.filter(status=1).count()       
        if depositcount == None:
            depositcount = 0
        if due == None:
            due = 0
        if payments == None:
            payments = 0
        return render(request, 'view_customers.html', {'std': std, 'customercount': customercount, 'payments': payments, 'depositcount': depositcount, 'invoice_count': invoice_count, 'due': due,'app':app})
    return redirect('loginfunc')

def Add_customer_details(request, pk):
    if 'supid' in request.session:
        customer = Customer_contact.objects.get(id=pk)
        customer_main = Customer.objects.get(id=customer.customer_id)
        if request.method == 'POST':
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
            customer.save()
            customer_main.save()
            return HttpResponse('true')
        
        return render(request, 'edit_customer.html',{'customer_main':customer_main,'customer':customer})
    return redirect('loginfunc')

def deletecustomer(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            contract = Contract.objects.filter(
                customer_contact_id=pk, status=1)
            if contract:
                return HttpResponse("False")
            else:
                std = Customer_contact.objects.get(id=pk)
                std.status = 2
                login=login_table.objects.get(customer_id=std.id)
                login.status =2
                login.save()
                std.save()
                return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')

def activatecustomer(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Customer_contact.objects.get(id=pk)
            std.status = 1
            login=login_table.objects.get(customer_id=std.id)
            login.status =1
            login.save()
            std.save()
            return HttpResponse("Activated")
    return redirect('loginfunc')

def activateuser(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            login=login_table.objects.get(id=pk)
            login.status =1
            login.save()
            return HttpResponse("Activated")
    return redirect('loginfunc')

def progress(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Customer_contact.objects.get(id=pk)
            std.status = 5
            std.save()
            return HttpResponse("Activated")
    return redirect('loginfunc')

def prospective(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Customer_contact.objects.get(id=pk)
            std.status = 3
            std.save()
            return HttpResponse("Activated")
    return redirect('loginfunc')

def Approvecontract(request):
    if 'supid' in request.session:
        std = Contract.objects.filter(status=3)
        return render(request, 'approve_contract.html', {'std': std})
    return redirect('loginfunc')

@api_view(['POST'])
def Approved_contract(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Contract.objects.get(id=pk)
            std.status = 1
            std.save()
            space = Space.objects.get(id=std.master_space_id)
            space.vacancy_status = 2
            space.save()
            admins = login_table.objects.filter(usertype=1)
            message = f"Contract #{std.contract_no} has been approved"
            for admin in admins:
                notification = Notification.objects.create(message=message, status=1, type=8)
                admin.notifications.add(notification)
            return Response("Approved Successfully")
    return redirect('loginfunc')

@api_view(['POST'])
def Rejected_contract(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Contract.objects.get(id=pk)
            std.status = 3
            std.save()
            admins = login_table.objects.filter(usertype=1)
            message = f"Contract #{std.contract_no} has been rejected"
            for admin in admins:
                notification = Notification.objects.create(message=message, status=1, type=8)
                admin.notifications.add(notification)
            return Response("Rejected Successfully")
    return redirect('loginfunc')

def Approveregistration(request, pk):
    if 'supid' in request.session:
        std = Customer_contact.objects.get(id=pk)
        return render(request, 'customer-registration-details.html', {'std': std})
    return redirect('loginfunc')

def Approvecustomer(request):
    if 'supid' in request.session:
        std = Customer_contact.objects.filter(status__in=['3', '5'])
        return render(request, 'approve_customer.html', {'std': std})
    return redirect('loginfunc')

@api_view(['POST'])
def Approved_customer(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            login_id = request.session['supid']
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            std = Customer_contact.objects.get(id=pk)
            std.status = 1
            std1 = login_table(login_name=std.customer.customer_name,
                               username=std.username, password=std.password,
                               usertype=2, status=1, created_on=date,
                               created_by=login_id, updated_on=date,
                               updated_by=login_id, email=std.email,
                               phno=std.phone_number, customer_id=std.id)
            std1.save()
            std.save()
            return Response("Approved Successfully")
    return redirect('loginfunc')

@api_view(['POST'])
def Rejected_customer(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Customer_contact.objects.get(id=pk)
            std.status = 4
            std.save()
            return Response("Rejected Successfully")
    return redirect('loginfunc')

def Add_contracts(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dates = datetime.now().strftime('%Y-%m-%d')
        customer = Customer_contact.objects.filter(status=1)
        masterspace = Space.objects.filter(status=1, vacancy_status=1)
        if request.method == 'POST':
            customer_id = request.POST['customername']
            spacename = request.POST['masterspace']
            contractno = request.POST['contractno']
            agreementno = request.POST['agreementno']
            agreementdate = request.POST['agreementdate']
            auctionno = request.POST['auctionno']
            auctiondate = request.POST['auctiondate']
            auctionnoticeno = request.POST['auctionnoticeno']
            auctionnoticenodate = request.POST['auctionnoticenodate']
            finalallotmentorderno = request.POST['finalallotmentorderno']
            finalallotmentordernodate = request.POST['finalallotmentordernodate']
            auctionnoticerefno = request.POST['auctionnoticerefno']
            auctionnoticerefnodate = request.POST['auctionnoticerefnodate']
            rfp_number = request.POST['rfp_number']
            fitment = request.POST['fitment']
            lockin = request.POST['lockin']
            rfp_date = request.POST['rfp_date']
            rfp_ref_number = request.POST['rfp_ref_number']
            rfp_ref_date = request.POST['rfp_ref_date']
            loa_number = request.POST['loa_number']
            loa_date = request.POST['loa_date']
            invoice_start_date = request.POST['invoice_start_date']
            tenure_start_date = request.POST['tenure_start_date']
            tenure_end_date = request.POST['tenure_end_date']
            contract_period = request.POST['contract_period']
            bill_start_date = request.POST['bill_start_date']
            rent_amount = request.POST['rent_amount']
            utility_charges = request.POST['utility_charges']
            cam_charges = request.POST['cam_charges']
            security_deposit = request.POST['security_deposit']
            hikes = request.POST['hikes']
            auth_sign = request.POST['auth_sign']
            desiginations = request.POST['desiginations']
            sq_ft_rate = request.POST['sq_ft_rate']
            std = Contract(customer_contact_id=customer_id,
                           master_space_id=spacename,
                           contract_no=contractno,
                           agreement_number=agreementno,
                           agreement_date=agreementdate,
                           auction_number=auctionno,
                           auction_date=auctiondate,
                           sq_ft_rate=sq_ft_rate,
                           auction_notice_number=auctionnoticeno,
                           auction_notice_date=auctionnoticenodate,
                           final_allotment_order_number=finalallotmentorderno,
                           final_allotment_order_date=finalallotmentordernodate,
                           auction_notice_ref_number=auctionnoticerefno,
                           auction_notice_ref_date=auctionnoticerefnodate,
                           rfp_number=rfp_number,
                           rfp_date=rfp_date,
                           rfp_ref_number=rfp_ref_number,
                           rfp_ref_date=rfp_ref_date,
                           loa_number=loa_number,
                           loa_date=loa_date,
                           invoice_start_date=invoice_start_date,
                           tenure_start_date=tenure_start_date,
                           tenure_end_date=tenure_end_date,
                           contract_period=contract_period,
                           fitment_period=fitment,
                           lock_in_period=lockin,
                           bill_start_date=bill_start_date,
                           rent_amount=rent_amount,
                           utility_charges=utility_charges,
                           cam_charges=cam_charges,
                           security_deposit=security_deposit,
                           hikes=hikes,
                           auth_sign=auth_sign,
                           desiginations=desiginations,
                           status=3,
                           created_on=date,
                           created_by_id=login_id,
                           )
            admins = login_table.objects.filter(usertype=1)
            message = f"A new contract has been created"
            for admin in admins:
                notification = Notification.objects.create(message=message, status=1, type=7)
                admin.notifications.add(notification)
            std.save()
            if 'rfpdatepic' in request.FILES:
                file = request.FILES['rfpdatepic']
                fs = FileSystemStorage(location='media/')
                filename = 'contract.jpg'
                saved_file = fs.save(filename, file)
                url = fs.url(saved_file)
                upload = ContractUpload(
                    contract_id=std.id,
                    contracttype = 1,
                    created_on = dates,
                    created_by_id=login_id,
                    file=url
                )
                upload.save()
            if 'auctiondatepic' in request.FILES:
                file = request.FILES['auctiondatepic']
                fs = FileSystemStorage(location='media/')
                filename = 'contract.jpg'
                saved_file = fs.save(filename, file)
                url = fs.url(saved_file)
                upload = ContractUpload(
                    contract_id=std.id,
                    contracttype = 2,
                    created_on = dates,
                    created_by_id=login_id,
                    file=url
                )
                upload.save() 
            if 'auctionnoticenodatepic' in request.FILES:
                file = request.FILES['auctionnoticenodatepic']
                fs = FileSystemStorage(location='media/')
                filename = 'contract.jpg'
                saved_file = fs.save(filename, file)
                url = fs.url(saved_file)
                upload = ContractUpload(
                    contract_id=std.id,
                    contracttype = 3,
                    created_on = dates,
                    created_by_id=login_id,
                    file=url
                )
                upload.save()
            return HttpResponse('Succesfully Inserted')
        return render(request, 'add_contract.html', {'customer': customer, 'masterspace': masterspace, })
    return redirect('loginfunc')

def View_contract(request):
    if 'supid' in request.session:
        std = Contract.objects.all().order_by('-id')
        spaces = Space.objects.filter(status=1)
        customers = Customer_contact.objects.filter(status=1)
        contractcount = Contract.objects.filter(status=1).count()
        depositcount = Contract.objects.filter(
            status=1).aggregate(TOTAL=Sum('security_deposit'))['TOTAL']
        rent = Contract.objects.filter(
            status=1).aggregate(TOTAL=Sum('rent_amount'))['TOTAL']
        if depositcount == None:
            depositcount=0
        if rent == None:
            rent =0
        current_date = timezone.now().date()
        # Update the status of contract in bulk
        contract =Contract.objects.filter(status=1, tenure_end_date__lt=current_date)
        if contract:
            for p in contract:
                p.status=2
                space = Space.objects.get(id=p.master_space_id)
                space.vacancy_status = 1
                contracts = Contract.objects.filter(customer_contact_id=p.customer_contact_id, status=1).count()
                if contracts == 1:
                    customer = Customer_contact.objects.get(id=p.customer_contact_id)
                    customer.status = 2
                    login=login_table.objects.get(customer_id=customer.id)
                    login.status =2
                    login.save()
                    customer.save()
                space.save()
                p.save()
                customers = login_table.objects.filter(usertype=2) 
                message = f"{space.space_name} is available now "
                for admin in customers:
                    notification = Notification.objects.create(message=message,status=1,type=6)
                    admin.notifications.add(notification)
                subject = 'New Rental Space Available'
                message = f'Hello,\n\nWe are excited to inform you that a new rental space is now available for you.\n\nDetails of the space:\n\nSpace Name: {space.space_name}\nArea: {space.area}sqft\nLocation: {space.metrostation.metrostation.station_name}\n\n If you are interested or have any questions, please feel free to contact us.\n\nThank you for being a valued customer.\n\nBest regards,\nThe KMRL Team'
                from_email = settings.EMAIL_HOST_USER
                customers= login_table.objects.filter(usertype=2,status=1)
                for p in customers:
                    to_email = p.email
                    send_mail(subject, message, from_email, [to_email])
        
        return render(request, 'view_contract.html', {'std': std, 'contractcount': contractcount, 'depositcount': depositcount, 'rent': rent, 'spaces': spaces, 'customers': customers})
    return redirect('loginfunc')

def deletecontract(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Contract.objects.get(id=pk)
            std.status = 2
            std.termination_date = timezone.now().date()
            spaces = Space.objects.get(id=std.master_space_id)
            spaces.vacancy_status = 1
            contract = Contract.objects.filter(
                customer_contact_id=std.customer_contact_id, status=1).count()
            if contract == 1:
                customer = Customer_contact.objects.get(
                    id=std.customer_contact_id)
                customer.status = 2
                login=login_table.objects.get(customer_id=customer.id)
                login.status =2
                login.save()
                customer.save()
            std.save()
            spaces.save()
            customers = login_table.objects.filter(usertype=2) 
            message = f"{spaces.space_name} is available now "
            for admin in customers:
                notification = Notification.objects.create(message=message,status=1,type=6)
                admin.notifications.add(notification)
            return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')

def Update_contracts(request, pk):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        customer = Customer_contact.objects.filter(status__in=['1','2'])
        masterspace = Space.objects.filter(status=1, vacancy_status=1)
        if request.method == 'POST':
            std = Contract.objects.get(id=pk)
            # Store the previous master space ID
            previous_master_space_id = std.master_space_id
            std.customer_contact_id = request.POST['customername']
            std.master_space_id = request.POST['masterspace']
            std.contract_no = request.POST['contractno']
            std.agreement_number = request.POST['agreementno']
            std.agreement_date = request.POST['agreementdate']
            std.auction_number = request.POST['auctionno']
            std.auction_date = request.POST['auctiondate']
            std.auction_notice_number = request.POST['auctionnoticeno']
            std.auction_notice_date = request.POST['auctionnoticenodate']
            std.final_allotment_order_number = request.POST['finalallotmentorderno']
            std.final_allotment_order_date = request.POST['finalallotmentordernodate']
            std.auction_notice_ref_number = request.POST['auctionnoticerefno']
            std.auction_notice_ref_date = request.POST['auctionnoticerefnodate']
            std.rfp_number = request.POST['rfp_number']
            std.fitment_period = request.POST['fitment']
            std.lock_in_period = request.POST['lockin']
            std.rfp_date = request.POST['rfp_date']
            std.rfp_ref_number = request.POST['rfp_ref_number']
            std.rfp_ref_date = request.POST['rfp_ref_date']
            std.loa_number = request.POST['loa_number']
            std.loa_date = request.POST['loa_date']
            std.invoice_start_date = request.POST['invoice_start_date']
            std.sq_ft_rate = request.POST['sq_ft_rate']
            std.tenure_start_date = request.POST['tenure_start_date']
            std.tenure_end_date = request.POST['tenure_end_date']
            std.contract_period = request.POST['contract_period']
            std.bill_start_date = request.POST['bill_start_date']
            std.rent_amount = request.POST['rent_amount']
            std.utility_charges = request.POST['utility_charges']
            std.cam_charges = request.POST['cam_charges']
            std.security_deposit = request.POST['security_deposit']
            std.hikes = request.POST['hikes']
            std.auth_sign = request.POST['auth_sign']
            std.desiginations = request.POST['desiginations']
            std.updated_on = date
            std.updated_by = login_id
            if std.tenure_end_date >= date:
                std.status = 1
                customers = Customer_contact.objects.get(
                    id=std.customer_contact_id)
                customers.status = 1
                login=login_table.objects.get(customer_id=customers.id)
                login.status =1
                login.save()
                customers.save()
            std.status = 3
            std.save()
            if 'agreementdatepic' in request.FILES:
                contract= ContractUpload.objects.get(contract_id=pk,contracttype=1)
                file = request.FILES['agreementdatepic']
                filename = 'contractupdated.jpg'
                fs = FileSystemStorage(location='media/')
                saved_file = fs.save(filename, file)
                url = fs.url(saved_file)
                contract.file = url
                contract.updated_on = date
                contract.updated_by = login_id
                contract.save()
            if 'auctiondatepic' in request.FILES:
                contract= ContractUpload.objects.get(contract_id=pk,contracttype=2)
                file = request.FILES['auctiondatepic']
                filename = 'contractupdated.jpg'
                fs = FileSystemStorage(location='media/')
                saved_file = fs.save(filename, file)
                url = fs.url(saved_file)
                contract.file = url
                contract.updated_on = date
                contract.updated_by = login_id
                contract.save()
            if 'auctionnoticenodatepic' in request.FILES:
                contract= ContractUpload.objects.get(contract_id=pk,contracttype=3)
                file = request.FILES['auctionnoticenodatepic']
                filename = 'contractupdated.jpg'
                fs = FileSystemStorage(location='media/')
                saved_file = fs.save(filename, file)
                url = fs.url(saved_file)
                contract.file = url
                contract.updated_on = date
                contract.updated_by = login_id
                contract.save()
            # Update vacancy status of previous master space
            previous_master_space = Space.objects.get(
                id=previous_master_space_id)
            if previous_master_space.vacancy_status == 2:
                previous_master_space.vacancy_status = 1
                previous_master_space.save()
            # Update vacancy status of current master space
            current_master_space = Space.objects.get(id=std.master_space_id)
            current_master_space.vacancy_status = 2
            current_master_space.save()
            space = Space.objects.get(id=std.master_space_id)
            space.vacancy_status = 2
            space.save()
            if std.status == 3:
                admins = login_table.objects.filter(usertype=1)
                message = f"Contract #{std.contract_no} has been edited"
                for admin in admins:
                    notification = Notification.objects.create(message=message, status=1, type=7)
                    admin.notifications.add(notification)
            if std.tenure_end_date < date:
                customers = login_table.objects.filter(usertype=2) 
                message = f"{previous_master_space.space_name} is available now "
                for admin in customers:
                    notification = Notification.objects.create(message=message,status=1,type=6)
                    admin.notifications.add(notification)
            return HttpResponse('Updated Succesfully ')
        std = Contract.objects.get(id=pk)
        return render(request, 'update_contracts.html', {'customer': customer, 'masterspace': masterspace, 'std': std, })
    return redirect('loginfunc')

def View_details_contract(request, pk):
    if 'supid' in request.session:
        std = Contract.objects.get(id=pk)
        spaces = Space.objects.filter(master_space_id=std.master_space_id)
        customer = Customer_contact.objects.get(id=std.customer_contact_id)
        contractpic = ContractUpload.objects.filter(contract_id=std.id)
        try:
            user_update = login_table.objects.get(id=std.updated_by)
        except login_table.DoesNotExist:
            user_update = ''
        context = {
            'std': std,
            'updated': user_update, 'spaces': spaces, 'customer': customer,'contractpic':contractpic
        }
        return render(request, 'view_details_contract.html', context)
    return redirect('loginfunc')

def Customer_contracts(request, pk):
    if 'supid' in request.session:
        std = Customer_contact.objects.get(id=pk)
        deposit = Contract.objects.filter(customer_contact_id=pk, status=1).aggregate(TOTAL=Sum('security_deposit'))['TOTAL']
        if deposit == None:
            deposit = 0
        contract = Contract.objects.filter(customer_contact_id=pk, status__in=['1', '2']).count()
        invoices = Invoices.objects.filter(customer_contact_id=pk).count()
        payment = Payments_Data.objects.filter(customer_id=pk).aggregate(Total=Sum('payment_amount'))['Total']
        due = Invoices.objects.filter(customer_contact_id=pk, status__in=['2', '4']).aggregate(Total=Sum('total_amount'))['Total']
        if due == None:
            due = 0
        if payment == None:
            payment = 0

        context = {'std': std, 'deposit': deposit,
                   'contract_count': contract, 'invoice_count': invoices, 'due': due, 'payment': payment}
        return render(request, 'customer_contract.html', context)
    return redirect('loginfunc')

def Invoice(request):
    if 'supid' in request.session:
        current_month = datetime.now().month
        customer = Customer_contact.objects.filter(status=1)
        std = Invoices.objects.all().order_by('-id')
        invoicecount = Invoices.objects.all().count()
        invoice = Invoices.objects.filter(status=1, invoice_issue_date__month=current_month).count()
        paidcount = Invoices.objects.filter(status=3).count()
        pendindcount = Invoices.objects.filter(status=2).count()
        overdue = Invoices.objects.filter(status=4).count()
        cancelcount = Invoices.objects.filter(status=5).count()
        draft = Invoices.objects.filter(status=1).count()
        current_date = timezone.now().date()
        Invoices.objects.filter(status=2, due_date__lt=current_date).update(status=4)
        return render(request, 'all_invoices.html', {'std': std, 'invoicecount': invoicecount, 'customer': customer, 'paid': paidcount, 'pending': pendindcount, 'draft': draft, 'cancel': cancelcount, 'overdue': overdue,'invoice':invoice})
    return redirect('loginfunc')

def Addinvoice(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d')
        customers = Customer_contact.objects.filter(status=1)
        masterspaces = Space.objects.filter(status=1)
        bank = Bank.objects.filter(status=1)
        try:
            company = Company_details.objects.latest('id')
        except Company_details.DoesNotExist:
            company = ''
        if request.method == 'POST':
            customer_id = request.POST['customername']
            masterspace = request.POST['spaces']
            contract = Contract.objects.get(master_space_id=masterspace)
            bank = request.POST['bank']
            totalamount = request.POST['totalamount']
            tax_amount_sum = request.POST['taxableAmount']
            cgst = request.POST['cgstsum']
            sgst = request.POST['sgstsum']
            invoice_no = request.POST['invoiceno']
            invoice_issue_date = request.POST['invoicedate']
            due_date = request.POST['duedate']
            irn_no = request.POST['irnno']
            ack_no = request.POST['ackno']
            ack_date = request.POST['ackdate']
            invoice_start_date = request.POST['invoicestart']
            invoice_end_date = request.POST['invoiceend']
            sac_code = request.POST['sac']
            taxable_amount = request.POST['taxamnt']
            maintanence = request.POST['maintanence']
            tax_percentage = request.POST['taxpercent']
            invoice = Invoices(
                invoice_no=invoice_no,
                customer_contact_id=customer_id,
                master_space_id=masterspace,
                contract_id=contract.id,
                bank_id=bank,
                invoice_issue_date=invoice_issue_date,
                company_id=company.id,
                total_amount=totalamount,
                tax_amount_sum=tax_amount_sum,
                cgst=cgst,
                sgst=sgst,
                due_date=due_date,
                irn_no=irn_no,
                ack_no=ack_no,
                ack_date=ack_date,
                invoice_start_date=invoice_start_date,
                invoice_end_date=invoice_end_date,
                sac_code=sac_code,
                taxable_amount=taxable_amount,
                maintanence=maintanence,
                tax_percentage=tax_percentage,
                created_on=date,
                created_by_id=login_id,
                status=1
            )
            invoice.save()
            return HttpResponse('Successfully Inserted')
        return render(request, 'add_invoice.html', {
            'customer': customers,
            'company': company,
            'masterspaces': masterspaces,
            'bank': bank,
        })
    return redirect('loginfunc')

def Create_all_invoices(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d')
        dates = datetime.now().date()
        customers = Customer_contact.objects.filter(status=1)
        masterspaces = Space.objects.filter(status=1)
        bank = Bank.objects.latest('id')
        try:
            company = Company_details.objects.latest('id')
        except Company_details.DoesNotExist:
            company = ''
        existing_invoice = False
        if request.method == 'POST':
            contracts = Contract.objects.filter(status=1)
            # Get the maximum invoice number
            max_invoice_number = Invoices.objects.aggregate(Max('invoice_no'))['invoice_no__max'] or 0
            max_ackno = Invoices.objects.aggregate(Max('ack_no'))['ack_no__max'] or 1516278315551
            # Calculate the invoice start date and end date
            _, last_day = monthrange(dates.year, dates.month)
            invoice_start_date = datetime(dates.year, dates.month, 1).strftime('%Y-%m-%d')
            invoice_end_date = datetime(dates.year, dates.month, last_day).strftime('%Y-%m-%d')
            for p in contracts:
                maintanence = 0
                tax_amount_sum = p.rent_amount + maintanence
                # Check if an invoice already exists for the current month and contract
                existing_invoice = Invoices.objects.filter(
                    Q(contract_id=p.id) & Q(invoice_issue_date__year=dates.year,
                                            invoice_issue_date__month=dates.month) & Q(status__in=['1','2','3','4'])
                ).exists()
                if existing_invoice:
                    continue  # Skip creating a new invoice if one already exists for the current month and contract
                max_invoice_number += 1
                max_ackno += 1
                Invoices.objects.create(
                    invoice_no=max_invoice_number,
                    customer_contact_id=p.customer_contact_id,
                    master_space_id=p.master_space_id,
                    contract_id=p.id,
                    bank_id=bank.id,
                    company_id=company.id,
                    invoice_issue_date=date,
                    tax_amount_sum=tax_amount_sum,
                    cgst=round(p.rent_amount * (9 / 100), 2),
                    sgst=round(p.rent_amount * (9 / 100), 2),
                    total_amount=round(
                        float(p.rent_amount) + float(round(p.rent_amount * (9 / 100), 2)) * 2, 2),
                    due_date=invoice_end_date,
                    irn_no='7c2903chwc9329e399ff3278fcc88678c9e999d87889sfv9990v954s67vs792defc1',
                    ack_no=max_ackno,
                    ack_date=date,
                    invoice_start_date=invoice_start_date,
                    invoice_end_date=invoice_end_date,
                    sac_code=997212,
                    taxable_amount=p.rent_amount,
                    maintanence=maintanence,
                    tax_percentage=9,
                    created_on=date,
                    created_by_id=login_id,
                    status=1
                )
            if existing_invoice:
                return HttpResponse('Already Exists')
            return HttpResponse('Invoice sent')
        return render(request, 'add_invoice.html', {
            'customer': customers,
            'company': company,
            'masterspaces': masterspaces,
            'bank': bank
        })
    return redirect('loginfunc')

def View_invoice(request, pk):
    if 'supid' in request.session:
        std = Invoices.objects.get(id=pk)
        contract = Contract.objects.filter(master_space_id=std.master_space_id)
        spaces = Space.objects.filter(master_space_id=std.master_space_id)
        spaces_count = Space.objects.filter(
            master_space_id=std.master_space_id).count()
        number = std.total_amount
        number_in_words = num2words(number, lang='en').title()
        return render(request, 'view_invoice.html', {'std': std, 'contract': contract, 'spaces': spaces, 'spaces_count': spaces_count, 'number_in_words': number_in_words})
    return redirect('loginfunc')

@api_view(['POST'])
def send_invoice(request, pk):
    if request.method == 'POST':
        std = Invoices.objects.get(id=pk)
        std.status = 2
        std.save()
        customers = login_table.objects.get(customer_id=std.customer_contact_id)
        message = f"You have received a new invoice"
        notification = Notification.objects.create(
                message=message, status=1, type=4)
        customers.notifications.add(notification)
        return Response('true')

@api_view(['POST'])
def send_all_invoice(request):
    if request.method == 'POST':
        current_month = datetime.now().month
        std = Invoices.objects.filter(status=1, invoice_issue_date__month=current_month)
        for p in std:
            p.status = 2
            p.save()
            customers = login_table.objects.get(customer_id=p.customer_contact_id)           
            message = f"You have received a new invoice"
            notification = Notification.objects.create(
            message=message, status=1, type=4)
            customers.notifications.add(notification)
        return Response('true')

def deleteinvoice(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Invoices.objects.get(id=pk)
            std.status = 5
            std.save()
            return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')

def Update_invoice(request, pk):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d')
        customers = Customer_contact.objects.filter(status=1)
        masterspaces = Space.objects.filter(status=1)
        bank = Bank.objects.filter(status=1)
        company = Company_details.objects.latest('id')
        if request.method == 'POST':
            std = Invoices.objects.get(id=pk)
            std.customer_contact_id = request.POST['customername']
            std.master_space_id = request.POST['spaces']
            std.bank_id = request.POST['bank']
            std.total_amount = request.POST['totalamount']
            std.tax_amount_sum = request.POST['taxableAmount']
            std.cgst = request.POST['cgstsum']
            std.sgst = request.POST['sgstsum']
            std.invoice_no = request.POST['invoiceno']
            std.invoice_issue_date = request.POST['invoicedate']
            std.due_date = request.POST['duedate']
            std.irn_no = request.POST['irnno']
            std.ack_no = request.POST['ackno']
            std.ack_date = request.POST['ackdate']
            std.invoice_start_date = request.POST['invoicestart']
            std.invoice_end_date = request.POST['invoiceend']
            std.sac_code = request.POST['sac']
            std.taxable_amount = request.POST['taxamnt']
            std.maintanence = request.POST['maintanence']
            std.tax_percentage = request.POST['taxpercent']
            std.updated_on = date
            std.updated_by = login_id
            std.save()
            return HttpResponse('Updated Succesfully ')
        std = Invoices.objects.get(id=pk)

        return render(request, 'update_invoice.html', {'std': std, 'customers': customers, 'masterspaces': masterspaces, 'bank': bank, 'company': company})
    return redirect('loginfunc')

def Payments(request):
    if 'supid' in request.session:
        customer = Customer_contact.objects.filter(status=1)
        std = Payments_Data.objects.filter(status__in=['1', '2', '3']).order_by('-id')
        payment_count = Payments_Data.objects.filter().count()
        payment_paid = Payments_Data.objects.filter(status=1).count()
        payment_pending = Payments_Data.objects.filter(status=2).count()
        payment_declined = Payments_Data.objects.filter(status=3).count()
        return render(request, 'payments.html', {'std': std, 'payment_count': payment_count, 'payment_paid': payment_paid, 'payment_pending': payment_pending, 'payment_declined': payment_declined, 'customer': customer})
    return redirect('loginfunc')

def Payment_report(request):
    if 'supid' in request.session:
        std = Payments_Data.objects.filter(status=1).order_by('-id')
        customer = Customer_contact.objects.filter(status=1)
        return render(request, 'payment_report.html', {'std': std, 'customer': customer})
    return redirect('loginfunc')

def Manage_users(request):
    if 'supid' in request.session:
        std = login_table.objects.filter(usertype__in=[ 3, 4, 5]).order_by('-id')
        return render(request, 'manage_users.html', {'std': std})
    return redirect('loginfunc')

def Profile_settings(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        std = login_table.objects.get(id=login_id)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if request.method == 'POST':
            std = login_table.objects.get(id=login_id)
            std.login_name = request.POST['name']
            std.email = request.POST['email']
            std.phno = request.POST['phone']
            std.updated_on = date
            std.updated_by = login_id
            if 'pic' in request.FILES:
                profile_pic = request.FILES['pic']
                fs = FileSystemStorage(location='media/')
                filename = 'profilepicture.jpg'
                saved_file = fs.save(filename, profile_pic)
                url = fs.url(saved_file)
            else:
                url = std.profile_pic
            std.profile_pic = url
            std.save()
            return HttpResponse('Updated Succesfully ')

        std = login_table.objects.get(id=login_id)

        return render(request, 'profile_settings.html', {'std': std})
    return redirect('loginfunc')

def Bank_settings(request):
    if 'supid' in request.session:
        bank = Bank.objects.filter(status=1)
        return render(request, 'bank_details.html', {'bank': bank})
    return redirect('loginfunc')

def Add_bank_details(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if request.method == 'POST':
            bank_name = request.POST['bank_name']
            branch_name = request.POST['branch_name']
            ifsc_code = request.POST['ifsc_code']
            acc_no = request.POST['acc_no']
            upi_id = request.POST['upi_id']

            std = Bank(bank_name=bank_name,
                       branch_name=branch_name,
                       acc_no=acc_no,
                       ifsc_code=ifsc_code,
                       upi_id=upi_id,
                       status=1,
                       created_on=date,
                       created_by_id=login_id,
                       )
            std.save()
            return HttpResponse('Succesfully Inserted')

        return render(request, 'bank_details.html')
    return redirect('loginfunc')

def Update_bank_details(request, pk):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if request.method == 'POST':
            std = Bank.objects.get(id=pk)
            std.bank_name = request.POST['bank_name']
            std.branch_name = request.POST['branch_name']
            std.ifsc_code = request.POST['ifsc_code']
            std.acc_no = request.POST['acc_no']
            std.upi_id = request.POST['upi_id']
            std.updated_on = date
            std.updated_by = login_id
            std.save()
            return HttpResponse('Updated Succesfully ')
        std = Bank.objects.get(id=pk)

        return render(request, 'bank_details.html', {'std': std})
    return redirect('loginfunc')

def deletebank(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Bank.objects.get(id=pk)
            std.status = 2
            std.save()
            return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')

def Notfication_settings(request):
    if 'supid' in request.session:
        return render(request, 'notification_settings.html')
    return redirect('loginfunc')

def Change_password(request):
    if 'supid' in request.session:
        if request.method == "POST":
            current_password = request.POST['current_password']
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']
            id = request.session['supid']
            std = login_table.objects.get(id=id)
            matchpassword = check_password(current_password, std.password)
            if matchpassword:
                hashpassword = make_password(new_password)
                std.password = hashpassword
                std.save()
                return HttpResponse('true')
            else:
                return HttpResponse('false')
        return render(request, 'change_password.html')
    return redirect('loginfunc')

def Delete_account(request):
    if 'supid' in request.session:
        return render(request, 'delete_account.html')
    return redirect('loginfunc')

def Profile(request):
    if 'supid' in request.session:
        id = request.session['supid']
        std = login_table.objects.get(id=id)

        if request.method == 'POST':
            std = login_table.objects.get(id=id)
        return render(request, 'profile.html', {'std': std})
    return redirect('loginfunc')

def Add_company_details(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if request.method == 'POST':
            company_name = request.POST['companyname']
            city = request.POST['city']
            district = request.POST['district']
            state = request.POST['state']
            pincode = request.POST['pincode']
            address = request.POST['address']
            gst_no = request.POST['gst_no']
            pan_no = request.POST['pan_no']
            cin = request.POST['cin']
            phno1 = request.POST['phno1']
            phno2 = request.POST['phno2']
            fax = request.POST['fax']
            email = request.POST['email']
            website = request.POST['website']
            state_code = request.POST['state_code']
            if 'authsign' in request.FILES:
                signature = request.FILES['authsign']
                filename = 'sign.jpg'
                fs = FileSystemStorage(location='media/')
                saved_file = fs.save(filename, signature)
                url = fs.url(saved_file)
            else:
                url = None

            std = Company_details(company_name=company_name,
                                  city=city,
                                  district=district,
                                  state=state,
                                  pincode=pincode,
                                  address=address,
                                  gst_no=gst_no,
                                  pan_no=pan_no,
                                  cin=cin,
                                  phno1=phno1,
                                  phno2=phno2,
                                  fax=fax,
                                  email=email,
                                  website=website,
                                  state_code=state_code,
                                  signature=url,
                                  created_on=date,
                                  created_by_id=login_id,
                                  )
            std.save()
            return HttpResponse('Succesfully Inserted')

        return render(request, 'add_company_details.html')
    return redirect('loginfunc')

def View_company_details(request):
    if 'supid' in request.session:
        try:
            std = Company_details.objects.latest('id')
        except Company_details.DoesNotExist:
            std = ""
        return render(request, 'viewcompanydetails.html', {'std': std})
    return redirect('loginfunc')

def Update_company_details(request, pk):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        if request.method == 'POST':
            std = Company_details.objects.get(id=pk)
            std.company_name = request.POST['companyname']
            std.city = request.POST['city']
            std.district = request.POST['district']
            std.state = request.POST['state']
            std.pincode = request.POST['pincode']
            std.address = request.POST['address']
            std.gst_no = request.POST['gst_no']
            std.pan_no = request.POST['pan_no']
            std.cin = request.POST['cin']
            std.phno1 = request.POST['phno1']
            std.phno2 = request.POST['phno2']
            std.fax = request.POST['fax']
            std.email = request.POST['email']
            std.website = request.POST['website']
            std.state_code = request.POST['state_code']
            std.updated_on = date
            std.updated_by = login_id
            if 'authsign' in request.FILES:
                signature = request.FILES['authsign']
                filename = 'updatedsign.jpg'
                fs = FileSystemStorage(location='media/')
                saved_file = fs.save(filename, signature)
                url = fs.url(saved_file)
                std.signature = url
            else:
                url = None
            std.save()
            return HttpResponse('Updated Succesfully ')
        std = Company_details.objects.get(id=pk)

        return render(request, 'update_company_details.html', {'std': std})
    return redirect('loginfunc')

def View_grievances(request):
    if 'lid' in request.session:
        Id = request.session['lid']
        login = login_table.objects.get(id=Id)
        customer = Customer_contact.objects.get(id=login.customer_id)
        std = Customer_grievance.objects.filter(
            customer_contact_id=customer.id, status__in=['1', '2', '4']).order_by('-id')
        masterspaces = Contract.objects.filter(
            customer_contact_id=customer.id, status=1)
        return render(request, 'customer_grievance.html', {'std': std, 'masterspaces': masterspaces})
    return redirect('loginfunc')

def Add_grievance(request):
    if 'lid' in request.session:
        Id = request.session['lid']
        login = login_table.objects.get(id=Id)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if request.method == 'POST':
            reason = request.POST['reason']
            complaint = request.POST['complaintdetails']
            masterspace = request.POST['space']
            if 'photo' in request.FILES:
                complaint_pic = request.FILES['photo']
                fs = FileSystemStorage(location='media/')
                filename = 'greivence.jpg'
                saved_file = fs.save(filename, complaint_pic)
                url = fs.url(saved_file)
            else:
                url = None

            std = Customer_grievance(
                master_space_id=masterspace,
                reason=reason,
                complaint=complaint,
                customer_contact_id=login.customer_id,
                complaint_pic=url,
                status=1,
                created_on=date,
                created_by_id=Id,
            )
            std.save()
            # Send notification to admin
            admins = login_table.objects.filter(usertype=1)
            message = f"You have received a new message"
            for admin in admins:
                notification = Notification.objects.create(message=message, status=1, type=2, customer=std.id)
                admin.notifications.add(notification)

            return HttpResponse('Succesfully Inserted')

        return render(request, 'customer_grievance.html')
    return redirect('loginfunc')

def deletegrievance(request, pk):
    if 'lid' in request.session:
        if request.method == 'POST':
            std = Customer_grievance.objects.get(id=pk)
            std.status = 3
            std.save()
            return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')

def Update_grievance(request, pk):
    if 'lid' in request.session:
        Id = request.session['lid']
        login = login_table.objects.get(id=Id)
        customer = Customer_contact.objects.get(id=login.customer_id)
        masterspaces = Contract.objects.filter(
            customer_contact_id=customer.id, status=1)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if request.method == 'POST':
            std = Customer_grievance.objects.get(id=pk)
            std.master_space_id = request.POST['space']
            std.reason = request.POST['reason']
            std.complaint = request.POST['complaintdetails']
            std.updated_on = date
            std.updated_by = Id
            if 'photo' in request.FILES:
                complaint_pic = request.FILES['photo']
                filename = 'greivence.jpg'
                fs = FileSystemStorage(location='media/')
                saved_file = fs.save(filename, complaint_pic)
                url = fs.url(saved_file)
                std.complaint_pic = url
            else:
                url = None
            std.save()
            return HttpResponse('Updated Succesfully ')
        std = Customer_grievance.objects.get(id=pk)

        return render(request, 'customer_grievance.html', {'edit': std, 'masterspaces': masterspaces})
    return redirect('loginfunc')

def View_grievance_details(request, pk):
    if 'lid' in request.session:
        std = Customer_grievance.objects.get(id=pk)
        return render(request, 'customer_grievance_details.html', {'std': std})
    return redirect('loginfunc')

def View_customer_grievances(request):
    if 'supid' in request.session:
        customer = Customer_contact.objects.filter(status=1)
        std = Customer_grievance.objects.filter(
            status__in=['1', '2']).order_by('-id')
        total = Customer_grievance.objects.filter(
            status__in=['1', '2']).count()
        resolved = Customer_grievance.objects.filter(status=2).count()
        open = Customer_grievance.objects.filter(status=1).count()
        masterspaces = Space.objects.filter(status=1)
        return render(request, 'view_customer_grievances.html', {'std': std, 'customer': customer, 'masterspaces': masterspaces, 'total': total, 'resolved': resolved, 'open': open})
    return redirect('loginfunc')

def deletecustomergrievance(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Customer_grievance.objects.get(id=pk)
            std.status = 4
            std.save()
            return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')

def Customer_grievance_form(request, pk):
    if 'supid' in request.session:
        std = Customer_grievance.objects.get(id=pk)
        return render(request, 'customer_grievance_form.html', {'std': std})
    return redirect('loginfunc')

def ReplyMessage(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = Customer_grievance.objects.get(id=pk)
            std.reply = request.POST['reply']
            std.status = 2
            std.save()
            customers = login_table.objects.get(customer_id=std.customer_contact_id)
            message = f"You have received a new message"
            notification = Notification.objects.create(message=message, status=1, type=9, customer=pk)
            customers.notifications.add(notification)
            return HttpResponse("Reply Sent")
    return redirect('loginfunc')

def general_parameter(request):
    if 'supid' in request.session:
        std = General_parameter.objects.filter()
        return render(request, 'general_parameter.html', {'std': std})
    return redirect('loginfunc')

class Gpmodel_view(APIView):
    def post(self, request):
        gp_type = request.POST.get('gptype')
        gp_value = request.POST.get('gpvalue')
        General_parameter.objects.create(
            gp_type=gp_type, gp_value=gp_value, status=1)
        return Response('true')

def inactive_gp(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = General_parameter.objects.get(id=pk)
            std.status = 2
            std.save()
            return HttpResponse("true")
    return redirect('loginfunc')

def active_gp(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = General_parameter.objects.get(id=pk)
            std.status = 1
            std.save()
            return HttpResponse("true")
    return redirect('loginfunc')

@api_view(['POST'])    
def update_gp(request,pk):
    if 'supid' in request.session:
        std=General_parameter.objects.get(id=pk)
        std.gp_type=request.POST.get('gptype')
        std.gp_value=request.POST.get('gpvalue')
        std.save()
        return Response('true')

@api_view(['GET'])
def get_gptype(request,pk):
    myobj=General_parameter.objects.get(id=pk)
    my_serializer=GenralParameterSerializer(myobj)
    return Response(my_serializer.data)

@api_view(['GET'])
def select_masterspaces(request, pk):
    myobj = Contract.objects.filter(customer_contact_id=pk, status=1)
    my_serializer = SpaceModelSerializer(myobj, many=True)
    return Response(my_serializer.data)

@api_view(['GET'])
def view_bank(request, pk):
    myobj = Bank.objects.filter(id=pk, status=1)
    my_serializer = BankSerializer(myobj, many=True)
    return Response(my_serializer.data)

@api_view(['GET'])
def view_grievance(request, pk):
    myobj = Customer_grievance.objects.filter(id=pk)
    my_serializer = GrievanceSerializer(myobj, many=True)
    return Response(my_serializer.data)

@api_view(['GET'])
def view_adminprofile(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        user = login_table.objects.get(id=login_id)
        my_serializer = AdminSerializer(user)
        return Response(my_serializer.data)
    
def admin_mail(request):
    if request.method == 'POST':
        termination_date = request.POST.get('term_date')
        types = request.POST.get('type')
        contract_no = request.POST.get('no')
        subject=''
        if types == "1":
            subject = 'Contract Termination'
            message = f'Contract #{contract_no} has been terminated on {termination_date}'
            from_email = settings.EMAIL_HOST_USER
            admin= login_table.objects.filter(usertype=1,status=1)
            for p in admin:
                to_email = p.email
                send_mail(subject, message, from_email, [to_email])
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
