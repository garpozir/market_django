from django.shortcuts import render, HttpResponse
from .models import mahsool
def homeView(request):
    headers=mahsool.objects.all()
    for head in headers:
        amo=head.amount
        txt = '{pr:,}'
        amo=txt.format(pr=amo)
        head.amount=amo
    return render(request,'market/index.html', {'headers':headers})
