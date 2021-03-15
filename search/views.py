from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from donorreg.models import Donor

# Create your views here.

def srch(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'search.html', c)

def dlist(request):
    if request.method == 'POST':
        bgroup = request.POST.get('bgroup', '')
        city = request.POST.get('city', '')
        donors = Donor.objects.filter(blood_group=bgroup, city=city)
        return render(None, 'list.html', {'donors':donors, 'bgroup':bgroup})