from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from home.models import signupmodel


# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')


def news(request):
    return render(request,'news.html')

def signup(request):
   
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        sn=signupmodel(first_name=first_name,last_name=last_name,email=email,password=password,confirm_password=confirm_password)
        sn.save()
       
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def Contact(request):
    
    if request.method=="post":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        subject=request.POST.get('subject')
        cn=Contact(firstname=firstname,lastname=lastname,Subject=subject,Date=datetime.today())
        cn.save()
        print(cn)
    return render(request,'contact.html')


def services(request):
    return render(request,'services.html')




def forget(request):
    return render(request,'forget.html')



