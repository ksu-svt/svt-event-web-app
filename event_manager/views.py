from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'event_manager/index.html')

def login(request):
    if request.POST:
        user=request.POST['login-user']
        passwd=request.POST['login-pass']

        auth=authenticate(username=user,password=passwd)
        if auth is not None:
            if auth.is_active:
                login(request,auth)
                return HttpResponseRedirect("/index.html")
            else:
                return render(request,'event_manager/login.html',{'error_message':"User Not Active"})#display if user not active
        else:
            return render(request, 'event_manager/login.html', {'error_message': "Invalid Username or Password"})#display if invalid username/password or user doesn't exist


    return render(request,'event_manager/login.html')#login form
