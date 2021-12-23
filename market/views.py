from django.shortcuts import render, HttpResponse
from .models import mahsool
import socket
import requests
import platform

def buyView(request):
    re_code=request.GET['q']
    hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    try:
        ip_pub = requests.get('http://httpbin.org/ip').json()['origin']
    except:ip_pub='اینترنت ندارید'
    info_buy = 'gggggg'
    return render(request,'market/buy.html', {'info_buy':info_buy,
                                                'infor':ip_address,
                                                'ip_pub':ip_pub,
                                                'infor2':platform.system(),
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
