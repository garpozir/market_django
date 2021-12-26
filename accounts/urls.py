#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.urls import path
from .views import SignupView,LoginView,LogoutView
app_name='accounts'
urlpatterns=[
    path('signup/',SignupView,name='accounts'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView,name='logout')
]

