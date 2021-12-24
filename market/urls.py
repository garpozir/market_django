#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.urls import path,re_path
from .views import homeView,buyView

urlpatterns=[
    path('',homeView,name='index'),
    re_path(r'^buy/$',buyView,name='buy')
]
