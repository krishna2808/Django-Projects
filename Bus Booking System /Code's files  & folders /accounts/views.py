from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



from .models import *
# Create your views here.
def signup(request):
    # if request.method == 'POST':
    #     register = Register.objects
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password1 = request.POST['pass']
    #     password2 = request.POST['repass']
    #     if password1 == password2:
    #         # key = Register.objects
    #         # print("******************************************************************************************")
    #         # print(key)
    #         # r = Register.objects
    #         # print(type(r.email))
    #         # print(r.email)
    #         # # d = {'keys':key}
    #         # # for i in key.all:
    #         # #     print(i)
    #         # print('********************************************************************************************')
    #         if User.objects.filter(username=username):
    #             error = {'error': "User already exist "}
    #             return render(request, 'accounts/signup.html', error)
    #         elif User.objects.filter(email=email):
    #             error = {'error': "Email already exist "}
    #             return render(request, 'accounts/signup.html', error)
    #         else:
    #             user = User.objects.create_user(username=username, email=email, password=password1)
    #             # r.username = username
    #             # r.email = email
    #             # r.password = password1
    #             user.save()
    #             return redirect('signin')
    #     else:
    #         error = {'error': "Password isn't match"}
    #         return render(request, 'accounts/signup.html', error)
    # else:
    #     return render(request, 'accounts/signup.html')

    if request.method == 'POST':
        username = request.POST['username']
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        email = request.POST['email']
        # mobileno = request.POST['mobileno']
        password1 = request.POST['password']
        password2 = request.POST['repassword']
        if password1 == password2:
            # for register in registers.all():
            if User.objects.filter(username=username):
                error = {'error': "User already exist "}
                return render(request, 'accounts/signup.html', error)
            if User.objects.filter(email=email):
                error = {'error': "Email already exist "}
                return render(request, 'accounts/signup.html', error)
            else:
                user = User.objects.create_user(username, email, password1)
                # user.firs_name = firstname
                # user.last_name = lastname
                user.save()
                messages.success(request, "Your account has been successfully created")

                return redirect('signin')
        else:
            error = {'error': "Password isn't match"}
            return render(request, 'accounts/signup.html', error)

    else:
        return render(request, 'accounts/signup.html')






def signin(request):

    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['pass']
    #     user = auth.authenticate(username=username, password=password)
    #     if user != None:
    #         auth.login(request, user)
    #         return redirect('/')
    #     else:
    #         error = {'error': 'Invalid Username or Password'}
    #         return render(request, 'accounts/signin.html', error)
    # else:
    #     return render(request, 'accounts/signin.html')
    #


        if not request.user.is_authenticated:
            if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfully Logged In !!!')
                    return redirect('busDetails')
                else:
                    error = {'error': 'Invalid Credentials, Please try again '}
                    return render(request, 'accounts/signin.html', error)

            else:
                return render(request, 'accounts/signin.html')
                # return HttpResponse('404 - Not found')
        else:
            # return render(request, 'store/information.html')

            return render(request, 'accounts/signin.html')




def log_out(request):
    # if request.method == 'POST':
        logout(request)
        messages.success(request, "Successfully Logout Out")
        return redirect('home')
    # else:
    #     return render(request, 'accounts/logout.html')

