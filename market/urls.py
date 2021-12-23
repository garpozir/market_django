from django.urls import path
from .views import homeView,buyView

urlpatterns=[
    path('',homeView,name='index'),
    path(r'buy/',buyView,name='buy')
]
