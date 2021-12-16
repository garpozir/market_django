from django.shortcuts import render

def homeView(request):
    return render(request,template_name='market/index.html')
# Create your views here.
