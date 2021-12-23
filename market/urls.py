from django.urls import path,re_path
from .views import homeView,buyView

urlpatterns=[
    path('',homeView,name='index'),
    re_path(r'^buy/[0-9]{5}',buyView,name='buy')
]
