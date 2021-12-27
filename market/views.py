#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse
from .models import mahsool,comment
import socket
import requests
import platform,os
from persiantools.jdatetime import JalaliDate
from django.db.models import Max
from .forms import addcomment

def maximum(request):
    headers=mahsool.objects.aggregate(Max('amount'))
    headers=mahsool.objects.filter(amount=headers['amount__max'])
    try:
        for head in headers:
            amo=head.amount
            txt = '{pr:,}'
            amo=txt.format(pr=amo)
            head.amount=amo
    except:pass
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    try:
        ip_pub = requests.get('http://httpbin.org/ip').json()['origin']
    except:ip_pub='اینترنت ندارید'
    return render(request,'market/expensive.html',{'headers':headers,


                                                'infor':ip_address,
                                                'ip_pub':ip_pub,
                                                'infor2':platform.system(),
                })

def offer(request):
    headers=mahsool.objects.filter(ofer__gt=0)
    for head in headers:
        amo=head.amount
        txt = '{pr:,}'
        amo=txt.format(pr=amo)
        head.amount=amo
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    try:
        ip_pub = requests.get('http://httpbin.org/ip').json()['origin']
    except:ip_pub='اینترنت ندارید'
    return render(request,'market/offer.html',{'headers':headers,


                                                'infor':ip_address,
                                                'ip_pub':ip_pub,
                                                'infor2':platform.system(),
                })

def comment_fu(request):
    try:
        code_2=(re_code)
    except:
        return HttpResponse('با موفقیت انجام نشد'+' :( ')
    if str(request.user)=='AnonymousUser':
        return HttpResponse('ابتدا باید وارد شوید')
    if request.method=='POST':
        form=addcomment(request.POST)
        if form.is_valid():
            title=form.cleaned_data['name']
            email=form.cleaned_data['e_mail']
            comment2=form.cleaned_data['comment_text']
            comment=comment.objects.create(code=code_2,name=title,e_mail=email,
                                          comment_text=comment2,user=request.user)
            comment.save()
            return HttpResponse('با موفقیت انجام شد'+' :) ')
        return HttpResponse('با موفقیت انجام نشد'+' :( ')
def buyView(request):
    form =addcomment()
    chk=None
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    try:
        ip_pub = requests.get('http://httpbin.org/ip').json()['origin']
    except:ip_pub='اینترنت ندارید'
    re_code2=list(request.GET.keys())[0]
    global re_code
    re_code=request.GET[re_code2]
    headers2=comment.objects.filter(code=re_code)
    headers2i=''
    if headers2.count()==0:
        headers2i='هنوز هیچ پیامی برای این محصول ارسال نشده است'
    try:
        chk=True
        head=mahsool.objects.get(code=re_code)
    except:chk=False

    if chk==False:
        fnd='هیچی پیدا نشد '+'):'
        return render(request,'market/index.html',{'fnd':fnd,
                                                'infor':ip_address,
                                                'ip_pub':ip_pub,
                                                'infor2':platform.system(),
                })
    coden=head.userid
    coden=int(coden)
    coden+=1
    try:
        ihead=mahsool.objects.get(userid=str(coden))
        coden=ihead.code
    except:
        coden=re_code

    codeb=head.userid
    codeb=int(codeb)
    codeb-=1
    like_status=re_code
    try:
        ihead=mahsool.objects.get(userid=str(codeb))
        codeb=ihead.code
    except:
        codeb=re_code

    if re_code2=='like':
        with open(f'./market/static/{re_code}','w') as fd:
            fd.write('1')
            fd.close()
    elif re_code2=='dis':
        with open(f'./market/static/{re_code}','w') as fd:
            fd.write('0')
            fd.close()

    elif re_code2=='next':
        re_code=coden
    elif re_code2=='prev':
        re_code=codeb

    amo=head.amount
    takh=(head.ofer*amo)//100
    takh=amo-takh
    txt = '{pr:,}'
    amo=txt.format(pr=amo)
    head.amount=amo
    takh=txt.format(pr=takh)
    sp_date=str(head.data).split(' ')[0]
    sp_date=sp_date.split('-')
    int_year=int(sp_date[0])
    int_mont=int(sp_date[1])
    int_day=int(sp_date[2])
    persian_date=JalaliDate.to_jalali(int_year, int_mont, int_day)
    if os.path.isfile(f'./market/static/{like_status}'):
        with open(f'./market/static/{like_status}','r') as fd:
            sta_like=fd.read().strip()
            fd.close()
        if int(sta_like):sta_dislike='0'
        else:sta_dislike='1'
    else:
        sta_like='0';sta_dislike='0'
    if chk:
        return render(request,'market/buy.html', {'head':head,
                                                  'headers2':headers2,
                                                  'form':form,
                                                  'headers2i':headers2i,
                                              'coden':coden,
                                              'codeb':codeb,
                                                'infor':ip_address,
                                                'sta_like':sta_like,'sta_dislike':sta_dislike,
                                                'ip_pub':ip_pub,
                                                'infor2':platform.system(),
                                                'takh':takh,
                                                'persian_date':persian_date,
                                              })
def homeView(request):
    headers=mahsool.objects.all()
    for head in headers:
        amo=head.amount
        txt = '{pr:,}'
        amo=txt.format(pr=amo)
        head.amount=amo

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    try:
        ip_pub = requests.get('http://httpbin.org/ip').json()['origin']
    except:ip_pub='اینترنت ندارید'
    return render(request,'market/index.html', {'headers':headers,
                                                'infor':ip_address,
                                                'ip_pub':ip_pub,
                                                'infor2':platform.system(),

                                                })
