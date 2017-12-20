from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.template import loader

def index(request):
    template=loader.get_template('event_manager/index.html')
    return HttpResponse(template.render({}, request))

def auth_login(request):
    if request.POST:

        user=request.POST['login-user']
        passwd=request.POST['login-pass']
        #
        auth=authenticate(username=user,password=passwd)
        if auth is not None:

            if auth.is_active:
                login(request,auth)
                template = loader.get_template('event_manager/index.html')
                return HttpResponse(template.render({}, request))
            else:
                template = loader.get_template('event_manager/login.html')
                return HttpResponse(template.render({'error_message':"User Not Active"}, request))#not working
        else:
            template = loader.get_template('event_manager/login.html')
            return HttpResponse(template.render({'error_message': "Invalid Username or Password"}, request))

    template = loader.get_template('event_manager/login.html')
    return HttpResponse(template.render({}, request))
