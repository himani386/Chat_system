from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re
# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello World</h1>")


def about(request):
    return HttpResponse("<h1>About Page</h1>")


def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    mess=""
    if(email !="" and password !=""):
        user = authenticate(username=email,password = password)
        if(user is not None):
            mess= "you have logged in successfully"
            return redirect("dashboard")
        else:
            mess= "email and password are incorrect"
    
    return render(request , 'login.html' , {"mess":mess})

def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None 

def register(request):
    if(request.method == 'GET'):
         return render(request , 'registers.html' , {"errors":""})

    email=request.POST.get('email')
    password=request.POST.get('password')
    confirmpassword=request.POST.get('confirmpassword')
    errors=""
    
    if  not validate_email(email):
       errors="email is not a valid email address"

    if(password!=confirmpassword ):
        errors ="password and confirmpassword do not match"
    if( len(password)<8 or 15<len(password)):
       errors="password should be  between 8 and 15 characters"
    if(errors == ""):
        user = User.objects.create(email=email,username= email)
        user.set_password(password)
        user.is_superuser= True
        user.save()
        errors ="user saved successfully"
    print(email,password)
    print(confirmpassword)
    return render(request , 'registers.html' , {"errors":errors})


def dashboard(request):
    return render(request , 'dashboard.html' , {})
def forgetpassword(request):
    if (request.method == 'GET'):
        return render(request , 'forgetpassword.html' ,{})   
    email = request.POST.get('email')

    return render(request , 'forgetpassword.html' , {})