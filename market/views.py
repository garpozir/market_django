from django.shortcuts import render, HttpResponse
from .models import mahsool
import socket
import requests
import platform,os
from persiantools.jdatetime import JalaliDate

def buyView(request):
    
    re_code=request.GET['q']
    head=mahsool.objects.get(code=re_code)
    amo=head.amount
    takh=(head.ofer*amo)//100
    takh=amo-takh
    txt = '{pr:,}'
    amo=txt.format(pr=amo)
    head.amount=amo
    takh=txt.format(pr=takh)
    #print(head.img)
    sp_date=str(head.data).split(' ')[0]
    sp_date=sp_date.split('-')
    int_year=int(sp_date[0])
    int_mont=int(sp_date[1])
    int_day=int(sp_date[2])
    persian_date=JalaliDate.to_jalali(int_year, int_mont, int_day)
    hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    if os.path.isfile('./static/sta_like'):
        with open('./static/sta_like','r') as fd:
            sta_like=fd.read().strip()
            fd.close()
        if int(sta_like):sta_dislike='0'
        else:sta_dislike='1'
    else:
        sta_like='0';sta_dislike='0'
    try:
        ip_pub = requests.get('http://httpbin.org/ip').json()['origin']
    except:ip_pub='اینترنت ندارید'
    #info_buy = 'gggggg'
    return render(request,'market/buy.html', {'head':head,
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
    
## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    try:
        ip_pub = requests.get('http://httpbin.org/ip').json()['origin']
    except:ip_pub='اینترنت ندارید'
## printing the hostname and ip_address
#print(f"Hostname: {hostname}")
#print(f"IP Address: {ip_address}")
    return render(request,'market/index.html', {'headers':headers,
                                                'infor':ip_address,
                                                'ip_pub':ip_pub,
                                                'infor2':platform.system(),
                                                
                                                })
