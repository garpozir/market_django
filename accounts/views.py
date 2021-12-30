#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
import socket
import requests
import platform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login,logout

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
try:
    ip_pub = requests.get('http://httpbin.org/ip').json()['origin']
except:ip_pub='اینترنت ندارید'

def SignupView(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/')
        return HttpResponse('با موفقیت انجام نشد'+' :( ')
    form = UserCreationForm()

    return render(request,'accounts/signup.html',{'form':form,
                                                'infor':ip_address,
                                                'ip_pub':ip_pub,
                                                'infor2':platform.system(),
                                                 })

def LoginView(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/')
        return HttpResponse('با موفقیت انجام نشد'+' :( ')
    form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form,
                                                'infor':ip_address,
                                                'ip_pub':ip_pub,
                                                'infor2':platform.system(),
                                                })

def LogoutView(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')

