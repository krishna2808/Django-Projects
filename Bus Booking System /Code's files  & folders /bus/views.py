from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from .models import *

def home(request):
    if request.method == 'POST':
        try:
            btnSingIn = request.POST['signin']
            btnSingUp = request.POST['signup']
            print('**************************************************************88')
            print(btnSingIn)
            print(btnSingUp)
            return render(request, 'bus/home.html')
        except ValueError or MultiValueDictKeyError:
            print('************************Error**************************************88')



    else:
        return render(request, 'bus/home.html')

def busDetails(request):
    if request.method == 'POST':
        busFrom = request.POST['from']
        busTo = request.POST['to']
        details = BusDetails.objects.all()
        for bus in details:
            if bus.busFrom == busFrom and bus.busTo == busTo:
                detail = {'Busname': bus.busName, 'Bustime': bus.busTime, 'Busfrom': bus.busFrom, 'Busto': bus.busTo, 'Busticket': bus.busTicket}
                return render(request, 'bus/busDetails.html', detail)
        return render(request, 'bus/busDetails.html', {'error': 'Details not found'})

    else:
        return render(request, 'bus/busDetails.html')
def payment(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # print("Logged in")
             return render(request, 'bus/payment.html')

        else:
            print("Not logged in")


        return render(request, 'bus/home.html')
    else:

        return render(request, 'bus/payment.html')

def blog(request):
    return render(request, 'bus/blog.html')


def profile(request):
    userObject = None
    users = None
    if request.user.is_authenticated:
        # print("*****************************************")
        # print(request.user.username)
        # print(request.user.first_name)
        # print(request.user.is_superuser)
        # print(User.objects.all())
        # if request.method == 'POST':
        #     pass
        # else:
            userObject = request.user
            if request.user.is_superuser == True:
                users = User.objects.all()
            else:
                users = None
            return render(request, 'bus/profile.html', {'userObject': userObject, 'users': users})

    else:
        return render(request, 'bus/home.html', {'userObject': userObject, 'users': users, 'error':"Please First Login your Account"})


