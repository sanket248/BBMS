from django.urls import path 
from search.views import srch
from django.contrib.auth import views as auth_views 
from django.conf.urls import url 

urlpatterns = [ 
    url(r'ser/$', srch),
] 