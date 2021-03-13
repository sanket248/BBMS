from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'home_base.html', c)

def signup(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'signup.html', c)

def signup_add(request):
    if request.method == 'POST':
        uname = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        user = User.objects.create_user(uname, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return HttpResponseRedirect('/login/')
    
def login(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin/')
    else:
        msg = "your username/password is incorrect..."
        return render(request, 'login.html', {"msg": msg})

def loggedin(request):
    return render(request, 'loggedin.html', {"full_name":request.user.username})

def invalidlogin(request):
    msg = "your username/password is incorrect..."
    return render(request, 'login.html', {"msg": msg})

def logout(request):
    auth.logout(request)
    return render(None, 'logout.html')