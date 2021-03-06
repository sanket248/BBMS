from django.urls import path 
from donorreg.views import dreg, add, addsuccess
from django.contrib.auth import views as auth_views 
from django.conf.urls import url 

urlpatterns = [ 
     url(r'donor-reg/$', dreg),
     url(r'add-donor/$', add),
     url(r'addsuccess/$', addsuccess),
]