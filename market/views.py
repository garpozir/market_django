from django.shortcuts import render, HttpResponse
from .models import mahsool
def homeView(request):
    headers=mahsool.objects.all()[0]
    amo=headers.amount
    txt = '{pr:,}'
    amo=txt.format(pr=amo)
    headers.amount=amo
    return render(request,'market/index.html', {'headers':headers})
