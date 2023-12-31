from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .models import *
from app1.form import *

# Create your views here.

def home(request):
    return render(request,'base.html')

def user_signup(request):
    if request.method == 'POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if User.objects.filter(username=name,email=email,password=password).exists():
                messages.info(request,'username already exists!!!')
                print("already have")
        else:
                new_user=User.objects.create_user(name,email,password)
                new_user.save()
                return redirect(user_login)
    else:
            print('wrong password')
    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_login)
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect(user_login)

def add_item(request):
    d=detailsee()
    if request.method =='POST':
        d=detailsee(request.POST)
        if d.is_valid():
            d.save()
            return list(request)
    return render(request,'add.html',{'f':d})


def list(request):
    p=Order.objects.all()
    return render(request,'list.html',{'l':p})


    
    
