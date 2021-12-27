#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.urls import path,re_path
from .views import homeView,buyView,offer,maximum,comment_fu

urlpatterns=[
    path('',homeView,name='index'),
    re_path(r'^buy/$',buyView,name='buy'),
    re_path(r'^offer/$',offer,name='offer'),
    re_path(r'^expensive/$',maximum,name='maximum'),
    re_path(r'^comment/$',comment_fu,name='comment_fu'),
]
