from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.home,name='home'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register')
    # path('services',views.services,name='services'),
    # path('contact',views.contact,name='contact')
]