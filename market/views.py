from django.shortcuts import render
import requests, os

def homeView(request):
    url='https://divar.ir'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT+='/templates/market/index.html'
    r=requests.get(url)
    with open(PROJECT_ROOT,'w') as fd:
        fd.write(r.text)
        fd.close()
    return render(request,template_name='market/index.html')
