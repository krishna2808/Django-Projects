from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from .models import *
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        # mobileno = request.POST['mobileno']
        password1 = request.POST['pass']
        password2 = request.POST['repass']
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
                user.firs_name = firstname
                user.last_name = lastname
                user.save()
                messages.success(request, "Your account has been successfully created")

                return redirect('login')
        else:
            error = {'error': "Password isn't match"}
            return render(request, 'accounts/signup.html', error)

    else:
        return render(request, 'accounts/signup.html')

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully Logged In !!!')
                return redirect('information')
            else:
                error = {'error': 'Invalid Credentials, Please try again '}
                return render(request, 'accounts/login.html', error)

        else:
            return render(request, 'accounts/login.html')
            # return HttpResponse('404 - Not found')
    else:
        # return render(request, 'store/information.html')

        return redirect('information')
def log_out(request):
    # if request.method == 'POST':
        logout(request)
        messages.success(request, "Successfully Logout Out")
        return redirect('home')
    # else:
    #     return render(request, 'accounts/logout.html')



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
            return render(request, 'accounts/profile.html', {'userObject': userObject, 'users': users})

    else:
        return render(request, 'accounts/home.html', {'userObject': userObject, 'users': users, 'error':"Please First Login your Account"})

def home(request):
    return render(request, 'accounts/home.html')


# fm = SignUpForm(request.POST, instance=request.user)
#         if fm.is_valid():
#             mobile = fm.clean_data.get('
#             mobile')
#             username = fm.clear_data.get('username')
#             # messages.success(request, 'Account Create Successfully !! ')
#             fm.save()
#             SignUpForm(user=User.objects.filter(username=username).first(), mobile=mobile)
#
#     else:
#         fm = SignUpForm()
#     return render(request, 'accounts/signup.html', {'form': fm})

