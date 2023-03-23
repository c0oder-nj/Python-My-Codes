from audioop import reverse
from base64 import urlsafe_b64encode
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from user_login import settings
from django.core.mail import *
from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import rendertostring
# Super user
# username --> niraj  
# password --> Django@987

# Normal User
# username --> nirajUser
# password --> niraj


# Create your views here.
def home(request):
    return render(request, 'authentication/MinorT/minor1.html')
    # return render(request,)

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        user_name = request.POST.get('u_name')
        password = request.POST.get('pass1')
        pass2 = request.POST['pass2']
        # applying filters 
        if User.objects.filter(username=user_name):
            messages.error(request,"Username is already exists!/n Try another username")
            return redirect('signup')
        
        if User.objects.filter(email=email):
            messages.error(request,'Email is already exists')
            return redirect('signup')

        if len(user_name)>10:
            messages.error(request,'Username must be under 10 characters')
            return redirect("signup")

        if password!=pass2:
            messages.error(request,"Your password isn't matching")
            return redirect('signup')

        if not user_name.isalnum():
            messages.error(request,"Username must be alpha neumeric")
            return redirect('signup')

        
        my_user = User.objects.create_user(user_name,email,password)
        my_user.first_name = first_name
        my_user.last_name = last_name
        my_user.is_active = False
        my_user.save()

        messages.success(request,'Your account is succesfully created & we send you a mail regarding it')

        # welcome email
        subject = "Welcome to web based career guidance system"

        msg = "Hello "+ my_user.first_name + "!!\n"+"Welcome to our web base career guidnace system \n"+"We sent you a confirmation link in order to activate your account\n\n"+'Thanks and regards Niraj Chittodiya'
        from_email = settings.EMAIL_HOST_USER
        list_to = [my_user.email]
        send_mail(subject,msg,from_email,list_to,fail_silently=True)

        # Email address confirmation email
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ mine"
        # msg2 = render_to_string('email-confirmtaion.html',{
        #     'name':my_user.first_name,
        #     'domain':current_site.domain,
        #     'uid':urlsafe_b64encode(force_bytes(my_user.pk))
        # })
        
        return redirect('signin')
        # return HttpResponse('This is my response')
    return render(request,'authentication/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['password']

        user = authenticate(request,password=password,username=username)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,'authentication/base.html',{'username':username})
            # return base(request,fname)
        else:
            messages.error(request,'Bad credentials')
            redirect('/')
    return render(request,'authentication/signin.html')
    

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('/')

def base(request,fname):
    if request.method == 'POST':
        return render(request,'authentication/base.html',{'fname':fname})
    return redirect('/')