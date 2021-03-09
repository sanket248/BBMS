from django.urls import path 
from AboutUs.views import about
from django.contrib.auth import views as auth_views 
from django.conf.urls import url 

urlpatterns = [ 
    url(r'about/$', about),
] 