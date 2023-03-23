from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# nirajopbolte
# NirajOp07@IAM#
def home(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'home.html')
    # return HTTPResponse("This is my home page")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        # password.type = 'text'
        x = password


        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')