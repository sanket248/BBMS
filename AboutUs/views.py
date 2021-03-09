from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User

# Create your views here.

def about(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'about.html', c)