#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django import forms

class addcomment(forms.Form):
    name=forms.CharField(max_length=100,label='نام کاربری')
    e_mail= forms.EmailField(label='پست الکترونیکی')
    comment_text=forms.CharField(widget=forms.Textarea,max_length=2000,label='متن پیام')
