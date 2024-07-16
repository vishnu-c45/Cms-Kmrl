from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
import datetime
import json
from django.utils import timezone
from django.db.models import Sum
from .models import *
from datetime import datetime,timedelta 
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def view_utility(request):
    if 'did' in request.session:
        std = Utility.objects.filter(status=1)
        station = MetroStationContact.objects.all()
        return render(request, 'power.html', {'std': std, 'station':station})
    return redirect('loginfunc')

def Add_power(request):
    if 'did' in request.session:
        Id = request.session['did']
        # login = login_table.objects.get(id=Id)
        date = datetime.now().strftime('%Y-%m-%d')
        if request.method == 'POST':
            metro = request.POST['station']
            electricity = request.POST['power']
            if 'photo' in request.FILES:
                powerpic = request.FILES['photo']
                fs = FileSystemStorage(location='media/')
                filename = 'power.jpg'
                saved_file = fs.save(filename, powerpic)
                url = fs.url(saved_file)
            else:
                url = None

            std = Utility(
                metrostation_id=metro,
                power=electricity,
                powerpic=url,
                status=1,
                created_on=date,
                created_by_id=Id,
            )
            std.save()
            # # Send notification to admin
            # admins = login_table.objects.filter(usertype=1)
            # message = f"You have received a new message"
            # for admin in admins:
            #     notification = Notification.objects.create(message=message, status=1, type=2, customer=std.id)
            #     admin.notifications.add(notification)
            return HttpResponse('Succesfully Inserted')

        return render(request, 'power.html')
    return redirect('loginfunc')

def view_water(request):
    if 'did' in request.session:
        std = Utility.objects.filter(status=2)
        station = MetroStationContact.objects.all()
        return render(request, 'water.html', {'std': std, 'station':station})
    return redirect('loginfunc')

def Add_water(request):
    if 'did' in request.session:
        Id = request.session['did']
        # login = login_table.objects.get(id=Id)
        date = datetime.now().strftime('%Y-%m-%d')
        if request.method == 'POST':
            metro = request.POST['station']
            water = request.POST['water']
            if 'photo' in request.FILES:
                waterpic = request.FILES['photo']
                fs = FileSystemStorage(location='media/')
                filename = 'water.jpg'
                saved_file = fs.save(filename, waterpic)
                url = fs.url(saved_file)
            else:
                url = None

            std = Utility(
                metrostation_id=metro,
                water=water,
                waterpic=url,
                status=2,
                created_on=date,
                created_by_id=Id,
            )
            std.save()
            # # Send notification to admin
            # admins = login_table.objects.filter(usertype=1)
            # message = f"You have received a new message"
            # for admin in admins:
            #     notification = Notification.objects.create(message=message, status=1, type=2, customer=std.id)
            #     admin.notifications.add(notification)
            return HttpResponse('Succesfully Inserted')

        return render(request, 'water.html')    
    return redirect('loginfunc')

def deletewater(request, pk):
    if 'did' in request.session:
        if request.method == 'POST':
            std = Utility.objects.get(id=pk)
            std.status = 3
            std.save()
            return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')

def deletepower(request, pk):
    if 'did' in request.session:
        if request.method == 'POST':
            std = Utility.objects.get(id=pk)
            std.status = 3
            std.save()
            return HttpResponse("Successfully Deleted")
    return redirect('loginfunc')