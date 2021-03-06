from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from donorreg.models import Donor

# Create your views here.

def dreg(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'dreg.html', c)

def add(request):
    if request.method == 'POST':
        name = request.POST.get('dname','')
        cnum = request.POST.get('cnum','')
        bgroup = request.POST.get('bgroup','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        gender = request.POST.get('gender','')
        d = Donor(donor_name=name, contect_no=cnum, blood_group=bgroup, address=address, city=city, gender=gender)
        d.save()
        return HttpResponseRedirect('/donorreg/addsuccess/')

def addsuccess(request):
    msg = "Thank you for donating..."
    return render(request, 'dreg.html', {"msg": msg})