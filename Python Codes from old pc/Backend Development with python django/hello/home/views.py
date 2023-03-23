from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'minor.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,password=password,username=username)

        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'minor_login.html')

def register(request):
    return render(request,'minor_register.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('fname')
        phone = request.POST.get('m_num')
        email = request.POST.get('email')
        password = request.POST.get("password")

        contact = Contact(name=name,phone=phone,email=email,password=password,date=datetime.today())
        contact.save()
        messages.success(request,'Your Respones has been submitted!')

    return render(request,'contact.html')
