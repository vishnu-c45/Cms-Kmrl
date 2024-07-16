from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
import datetime
import json
from django.utils import timezone
from django.db.models import Sum, Count, Q
from .models import *
from .serializers import MyModelSerializer, InvoiceSerializer, PaymentSerializer, NotificationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
import json
from django.db.models.functions import ExtractMonth, ExtractYear


def firstapp(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        user = login_table.objects.get(id=login_id)
        notifications = user.notifications.filter(status=1)
        current_month = timezone.now().month
        current_year = timezone.now().year

        current_month_invoices = Payments_Data.objects.filter(
            status=1,
            created_on__month=current_month,
            created_on__year=current_year
        ).aggregate(total_invoice=Sum('payment_amount'))['total_invoice']

        current_year_invoices = Payments_Data.objects.filter(
            status=1,
            created_on__year=current_year
        ).aggregate(total_invoice=Sum('payment_amount'))['total_invoice']

        current_month_pending_invoices = Invoices.objects.filter(
            status__in=['2', '4'],
            invoice_issue_date__month=current_month,
            invoice_issue_date__year=current_year
        ).aggregate(total_invoice=Sum('total_amount'))['total_invoice']

        current_year_pending_invoices = Invoices.objects.filter(
            status__in=['2', '4'],
            invoice_issue_date__year=current_year
        ).aggregate(total_invoice=Sum('total_amount'))['total_invoice']

        current_month_water = Utility.objects.filter(
            status=2,
            created_on__month=current_month,
            created_on__year=current_year
        ).aggregate(total_water=Sum('water'))['total_water']

        current_year_water = Utility.objects.filter(
            status=2,
            created_on__year=current_year
        ).aggregate(total_water=Sum('water'))['total_water']

        current_month_power = Utility.objects.filter(
            status=1,
            created_on__month=current_month,
            created_on__year=current_year
        ).aggregate(total_power=Sum('power'))['total_power']

        current_year_power = Utility.objects.filter(
            status=1,
            created_on__year=current_year
        ).aggregate(total_power=Sum('power'))['total_power']

        vac_count = Space.objects.filter(status=1, vacancy_status=1).count()
        occ_count = Space.objects.filter(status=1, vacancy_status=2).count()
        space_count = Space.objects.filter(vacancy_status__in=['1', '2']).count()
        areasum = Space.objects.filter(status=1, vacancy_status__in=['1', '2']).aggregate(total_area=Sum('area'))['total_area']
        vacsum = Space.objects.filter(status=1, vacancy_status=1).aggregate(total_area=Sum('area'))['total_area']
        occsum = Space.objects.filter(status=1, vacancy_status=2).aggregate(total_area=Sum('area'))['total_area']
        invoicesum = Invoices.objects.filter(status__in=['2', '3', '4']).count()
        invoicepaid = Invoices.objects.filter(status__in=['3']).count()
        invoicepending = Invoices.objects.filter(status__in=['2', '4']).count()
        customercount = Customer_contact.objects.filter(status__in=['3', '5']).count()
        prospective = Customer_contact.objects.filter(status=3).count()
        inprogress = Customer_contact.objects.filter(status=5).count()
        active = Customer_contact.objects.filter(status=1).count()
        app = Customer_contact.objects.filter(status=1).count()
        depositcount = Contract.objects.filter(status=1).aggregate(TOTAL=Sum('security_deposit'))['TOTAL']
        depositpaid = Contract.objects.filter(status=1).aggregate(TOTAL=Sum('security_deposit'))['TOTAL']
        power = 10000
        powerused = Utility.objects.filter(status=1).aggregate(TOTAL=Sum('power'))['TOTAL']
        powerremaining = power-0
        water = 10000
        waterused = Utility.objects.filter(status=2).aggregate(TOTAL=Sum('water'))['TOTAL']
        waterremaining = water-0
        invoice_data = (
            Invoices.objects
            .annotate(month=ExtractMonth('invoice_issue_date'))
            .values('month')
            .annotate(invoice_count=Count('id'))
            .order_by('month').filter(status__in=['2', '4', '3'])
        )
        payment_data = (
            Payments_Data.objects
            .annotate(month=ExtractMonth('created_on'))
            .values('month')
            .annotate(payment_count=Count('id'))
            .order_by('month').filter(status=1)
        )

        invoice_data_list = list(invoice_data)
        invoice_data_json = json.dumps(invoice_data_list)
        payment_data_list = list(payment_data)
        payment_data_json = json.dumps(payment_data_list)

        invoice_data_by_year = (
            Invoices.objects
            .annotate(year=ExtractYear('invoice_issue_date'))
            .values('year')
            .annotate(invoice_count_year=Count('id'))
            .order_by('year').filter(status__in=['2', '4', '3'])
        )

        payment_data_by_year = (
            Payments_Data.objects
            .annotate(year=ExtractYear('created_on'))
            .values('year')
            .annotate(payment_count_year=Count('id'))
            .order_by('year').filter(status=1)
        )

        invoice_data_list_year = list(invoice_data_by_year)
        invoice_data_json_year = json.dumps(invoice_data_list_year)
        payment_data_list_year = list(payment_data_by_year)
        payment_data_json_year = json.dumps(payment_data_list_year)
        if power == None:
            power=0 
        if powerused == None:
            powerused=0    
        if powerremaining == None:
            powerremaining=0   
        if water == None:
            water=0 
        if waterused == None:
            waterused=0    
        if waterremaining == None:
            waterremaining=0  
        if current_month_invoices == None:
            current_month_invoices = 0
        if current_month_pending_invoices == None:
            current_month_pending_invoices = 0
        if current_year_invoices == None:
            current_year_invoices = 0
        if current_year_pending_invoices == None:
            current_year_pending_invoices = 0
        if depositcount == None:
            depositcount = 0
        if depositpaid == None:
            depositpaid = 0
        if areasum == None:
            areasum = 0
        if vacsum == None:
            vacsum = 0
        if occsum == None:
            occsum = 0
        invoice_list = Invoices.objects.all().order_by('-id')[:5]
        payments_lits = Payments_Data.objects.filter().order_by('-id')[:5]
        from_date = ''
        to_date = ''
        if request.method == 'POST':
            from_date = request.POST.get('fromDate')
            to_date = request.POST.get('toDate')
            if from_date and to_date:
                from_datetime = datetime.strptime(from_date, '%Y-%m-%d')
                to_datetime = datetime.strptime(to_date, '%Y-%m-%d')
                to_datetime += timedelta(days=1)
                space_count = Space.objects.filter(vacancy_status__in=['1', '2'], created_on__range=(from_datetime, to_datetime)).count()
                vac_count = Space.objects.filter(status=1, vacancy_status=1, created_on__range=(from_datetime, to_datetime)).count()
                occ_count = Space.objects.filter(status=1, vacancy_status=2, created_on__range=(from_datetime, to_datetime)).count()
                areasum = Space.objects.filter(status=1, vacancy_status__in=['1', '2'], created_on__range=(from_datetime, to_datetime)).aggregate(total_area=Sum('area'))['total_area']
                vacsum = Space.objects.filter(status=1, vacancy_status=1, created_on__range=(from_datetime, to_datetime)).aggregate(total_area=Sum('area'))['total_area']
                occsum = Space.objects.filter(status=1, vacancy_status=2, created_on__range=(from_datetime, to_datetime)).aggregate(total_area=Sum('area'))['total_area']
                invoicesum = Invoices.objects.filter(status__in=['2', '3', '4'], created_on__range=(from_datetime, to_datetime)).count()
                invoicepaid = Invoices.objects.filter(status__in=['3'], created_on__range=(from_datetime, to_datetime)).count()
                invoicepending = Invoices.objects.filter(status__in=['2', '4'], created_on__range=(from_datetime, to_datetime)).count()
                customercount = Customer_contact.objects.filter(status__in=['1', '2', '3', '5'], created_on__range=(from_datetime, to_datetime)).count()
                prospective = Customer_contact.objects.filter(status=3, created_on__range=(from_datetime, to_datetime)).count()
                inprogress = Customer_contact.objects.filter(status=5, created_on__range=(from_datetime, to_datetime)).count()
                active = Customer_contact.objects.filter(status=1, created_on__range=(from_datetime, to_datetime)).count()
                app = Customer_contact.objects.filter(status=1, created_on__range=(from_datetime, to_datetime)).count()
                depositcount = Contract.objects.filter(status=1, created_on__range=(from_datetime, to_datetime)).aggregate(TOTAL=Sum('security_deposit'))['TOTAL']
                depositpaid = Contract.objects.filter(status=1, created_on__range=(from_datetime, to_datetime)).aggregate(TOTAL=Sum('security_deposit'))['TOTAL']
                paidinvoice = Invoices.objects.filter(status=3, created_on__range=(from_datetime, to_datetime)).aggregate(total_invoice=Sum('total_amount'))['total_invoice']
                pendinginvoice = Invoices.objects.filter(status__in=['2', '4'], created_on__range=(from_datetime, to_datetime)).aggregate(total_invoice=Sum('total_amount'))['total_invoice']
                # power = 100000
                # powerused = Utility.objects.filter(status=1,created_on__range=(from_datetime, to_datetime)).aggregate(TOTAL=Sum('power'))['TOTAL']
                # powerremaining = power-powerused  
                if power == None:
                    power=0 
                if powerused == None:
                    powerused=0    
                if powerremaining == None:
                    powerremaining=0  
                if water == None:
                    water=0 
                if waterused == None:
                    waterused=0    
                if waterremaining == None:
                    waterremaining=0         
                if paidinvoice == None:
                    paidinvoice = 0
                if pendinginvoice == None:
                    pendinginvoice = 0
                if areasum == None:
                    areasum = 0
                if vacsum == None:
                    vacsum = 0
                if occsum == None:
                    occsum = 0
                if depositcount == None:
                    depositcount = 0
                if depositpaid == None:
                    depositpaid = 0
        context = {
            'invoice_list': invoice_list, 'payments_lits': payments_lits, 'vac': vac_count, 'occ': occ_count,
            'space': space_count, 'areasum': areasum, 'vacsum': vacsum, 'occsum': occsum, 'fromdate': from_date, 'todate': to_date,
            'not': notifications, 'invoicesum': invoicesum, 'invoicepaid': invoicepaid, 'invoicepending': invoicepending, 'customercount': customercount,
            'prospective': prospective, 'inprogress': inprogress, 'active': active,
            'app': app, 'depositcount': depositcount, 'depositpaid': depositpaid,
            'paidinvoice': current_month_invoices, 'pendinginvoice': current_month_pending_invoices,
            'paidinvoiceyear': current_year_invoices, 'pendinginvoiceyear': current_year_pending_invoices,
            'invoice_data_json': invoice_data_json, 'payment_data_json': payment_data_json,
            'invoice_data_json_year': invoice_data_json_year, 'payment_data_json_year': payment_data_json_year,
            'power':power,'powerused':powerused,'powerremaining':powerremaining,
            'water':water,'waterused':waterused,'waterremaining':waterremaining,
            'powerusedmonth':current_month_power,'powerusedyear':current_year_power,
            'waterusedmonth':current_month_water,'waterusedyear':current_year_water,
        }
        return render(request, "admin_dashboard.html", context)
    return redirect('loginfunc')

def loginfunc(request):
    return render(request, "sign-in.html")

def Viewmetrostaions(request):
    if 'supid' in request.session:
        std = MetroStationContact.objects.filter(status=1).order_by('-id')
        metrocount = MetroStationContact.objects.filter(status=1).count()
        spaces = Space.objects.filter(status=1).count()
        areasum = Space.objects.filter(
            status=1).aggregate(TOTAL=Sum('area'))['TOTAL']
        if areasum == None:
            areasum = 0
        return render(request, 'viewmetrostaion.html', {'std': std, 'metrocount': metrocount, 'spaces': spaces, 'areasum': areasum})
    return redirect('loginfunc')

def View_details_metrostation(request, pk):
    if 'supid' in request.session:
        std = MetroStationContact.objects.get(id=pk)
        user_create = login_table.objects.get(id=std.created_by)
        spaces_count = Space.objects.filter(
            metrostation_id=pk, status=1).count()
        space_details = Space.objects.filter(
            metrostation_id=pk, status=1).order_by('-id')
        occupied_space = Space.objects.filter(
            vacancy_status=2, metrostation_id=pk, status=1,).count()
        vaccant_spaces = Space.objects.filter(
            vacancy_status=1, metrostation_id=pk, status=1).count()
        office = Space.objects.filter(
            metrostation_id=pk, status=1, space_type='office').count()
        kiosk = Space.objects.filter(
            metrostation_id=pk, status=1, space_type='kiosk').count()
        areasum = Space.objects.filter(
            metrostation_id=pk, status=1).aggregate(TOTAL=Sum('area'))['TOTAL']
        if areasum == None:
            areasum = 0
        try:
            user_update = login_table.objects.get(id=std.updated_by)
        except login_table.DoesNotExist:
            user_update = ''
        context = {
            'std': std,
            'created': user_create,
            'updated': user_update, 'space_count': spaces_count,
            'space_details': space_details, 'occupied': occupied_space, 'vacant': vaccant_spaces,
            'office': office, 'kiosk': kiosk, 'areasum': areasum,
        }
        return render(request, 'view_details_metrostation.html', context)
    return redirect('loginfunc')

def Addmetrostaions(request):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if request.method == 'POST':
            stationname = request.POST['stationname']
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']
            s_name = request.POST['s_name']
            city = request.POST['city']
            district = request.POST['district']
            pincode = request.POST['pincode']
            email = request.POST['email']
            phone = request.POST['phone']
            status = 1
            std = Metrostation(station_name=stationname,
                               start_time=start_time,
                               s_name=s_name,
                               end_time=end_time,
                               status=1,
                               created_on=date,
                               created_by=login_id)
            std.save()
            std2 = MetroStationContact(metrostation_id=std.id,
                                       city=city,
                                       district=district,
                                       pincode=pincode,
                                       email=email,
                                       phone_number=phone,
                                       status=status,
                                       created_on=date,
                                       created_by=login_id)
            std2.save()
            return HttpResponse('successfully inserted')
        return render(request, 'add_metrostation.html')
    return redirect('loginfunc')


def Update_metrostation(request, pk):
    if 'supid' in request.session:
        login_id = request.session['supid']
        date = timezone.now()

        if request.method == 'POST':
            std = MetroStationContact.objects.get(id=pk)
            metro = Metrostation.objects.get(id=std.metrostation.id)
            metro.station_name = request.POST['stationname']
            metro.start_time = request.POST['start_time']
            metro.end_time = request.POST['end_time']
            std.city = request.POST['city']
            metro.s_name = request.POST['s_name']
            std.district = request.POST['district']
            std.pincode = request.POST['pincode']
            std.email = request.POST['email']
            std.phone_number = request.POST['phone']
            std.updated_on = date
            std.updated_by = login_id
            std.save()
            metro.save()
            return HttpResponse("updation successfully")
        std = MetroStationContact.objects.get(id=pk)
        return render(request, 'update_metrostation.html', {'std': std})
    return redirect('loginfunc')


def deletemetrostaion(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = MetroStationContact.objects.get(id=pk)
            std.status = 2
            std.save()
            return HttpResponse("successfully deleted")
    return redirect('loginfunc')


# End Metro Station ---------------------------./>


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        makepassword =make_password(password)
        print(makepassword)
        login_db = login_table.objects.filter(
            username=username, status=1)

        if login_db.exists():
            login_db = login_db[0]
            matchpassword = check_password(password, login_db.password)
            if matchpassword:
                if login_db.usertype == 1:
                    request.session['supid'] = login_db.id
                    return redirect('firstapp')

                elif login_db.usertype == 2:
                    request.session['lid'] = login_db.id
                    return redirect('customer_dasboard')

                elif login_db.usertype == 3:
                    request.session['fid'] = login_db.id
                    return redirect('')
                elif login_db.usertype == 4:
                    request.session[''] = login_db.id
                    return redirect('')
                elif login_db.usertype == 5:
                    request.session['did'] = login_db.id
                    return redirect('view_utility')
                else:
                    return redirect('loginfunc')
            else:
                messages.error(request, 'incorrect password')
                return redirect('signin')

        else:
            messages.error(request, 'Incorrect username')
            return redirect('signin')
    else:
        return render(request, 'sign-in.html')


def adduser(request):
    if 'supid' in request.session:
        if request.method == 'POST':
            usertype = request.POST['usertype']
            loginname = request.POST['loginname']
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['confirm_password']
            user = login_table.objects.filter(username=username)
            if user.exists():
                return HttpResponse('exists')
            else:
                if password == cpassword:
                    hashpassword = make_password(password)
                    std = login_table(usertype=usertype,
                                      login_name=loginname,
                                      username=username,
                                      password=hashpassword,
                                      status=1)
                    std.save()
                    return HttpResponse('true')
                else:
                    return HttpResponse('false')
        return render(request, 'add_users.html')
    else:
        return redirect('user_logout')

def Update_user(request, pk):
    if 'supid' in request.session:
        std = login_table.objects.get(id=pk)
        if request.method == 'POST':
            std = login_table.objects.get(id=pk)
            std.login_name = request.POST['loginname']
            std.username = request.POST['username']
            std.usertype = request.POST['usertype']
            password = request.POST['password']
            cpassword = request.POST['confirm_password']
            usertable = login_table.objects.filter(
                username=std.username, status=1).exclude(id=pk)
            if usertable.exists():
                return HttpResponse('exists')
            else:
                if password == cpassword:
                    hashpassword = make_password(password)
                    std.password = hashpassword
                    std.save()
                    return HttpResponse('true')
                else:
                    return HttpResponse('false')
        else:
            return render(request, 'edit_user.html', {'std': std})
    else:
        return redirect('user_logout')

def deleteuser(request, pk):
    if 'supid' in request.session:
        if request.method == 'POST':
            std = login_table.objects.get(id=pk)
            std.status = 2
            std.save()
            return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')

def user_logout(request):
    request.session.flush()
    return redirect('signin')

class NotificationAPIView(APIView):
    def get(self, request):
        if 'supid' in request.session:
            login_id = request.session['supid']
            user = login_table.objects.get(id=login_id)
            notifications = user.notifications.filter(status=1).order_by('-id')
            serializer = NotificationSerializer(notifications, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Not logged in.'})

    def post(self, request):
        if 'supid' in request.session:
            login_id = request.session['supid']
            user = login_table.objects.get(id=login_id)
            notifications = user.notifications.filter(status=1)

            for p in notifications:
                p.status = 2
                p.save()
            return HttpResponse('Notifications cleared successfully')

# Rest api...........................................
# .........Contract dtails in space ...............
@api_view(['GET'])
def space_details_contract(request, pk):
    myobj = Contract.objects.filter(master_space_id=pk, status__in=['1', '2'])
    my_serializer = MyModelSerializer(myobj, many=True)
    return Response(my_serializer.data)

@api_view(['GET'])
def space_details_customer(request, pk):
    myobj = Invoices.objects.filter(master_space_id=pk)
    my_serializer = InvoiceSerializer(myobj, many=True)
    return Response(my_serializer.data)

@api_view(['GET'])
def space_details_payments(request, pk):
    try:
        std = Contract.objects.get(master_space_id=pk)
        myobj = Payments_Data.objects.filter(
            master_space_id=std.master_space_id)
        my_serializer = PaymentSerializer(myobj, many=True)
        return Response(my_serializer.data)
    except Contract.DoesNotExist:
        my_serializer = []
        return Response(my_serializer)

# --------------Customer details in Space..............
@api_view(['GET'])
def Customer_detais_contract(request, pk):
    myobj = Contract.objects.filter(customer_contact_id=pk)
    my_serializer = MyModelSerializer(myobj, many=True)
    return Response(my_serializer.data)

@api_view(['GET'])
def Customer_details_invoice(request, pk):
    myobj = Invoices.objects.filter(customer_contact_id=pk)
    my_serializer = InvoiceSerializer(myobj, many=True)
    return Response(my_serializer.data)

@api_view(['GET'])
def Customer_details_payment(request, pk):
    myobj = Payments_Data.objects.filter(customer_id=pk)
    my_serializer = PaymentSerializer(myobj, many=True)
    return Response(my_serializer.data)

def IntrestSpaceView(request):
    if 'supid' in request.session:
        std =IntrestSpace.objects.all().order_by('-id')
        return render(request,'interst_space.html',{'spaces':std})