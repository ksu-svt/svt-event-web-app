from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .forms import UserCreateForm


def index(request):
    template=loader.get_template('event_manager/index.html')
    return HttpResponse(template.render({}, request))

#obselete method
# def auth_login(request):
#     if request.POST:
#
#         user=request.POST['login-user']
#         passwd=request.POST['login-pass']
#         #
#         auth=authenticate(username=user,password=passwd)
#         if auth is not None:
#
#             if auth.is_active:
#                 login(request,auth)
#                 template = loader.get_template('event_manager/index.html')
#                 return HttpResponse(template.render({}, request))
#             else:
#                 template = loader.get_template('event_manager/login.html')
#                 return HttpResponse(template.render({'error_message':"User Not Active"}, request))#not working
#         else:
#             template = loader.get_template('event_manager/login.html')
#             return HttpResponse(template.render({'error_message': "Invalid Username or Password"}, request))
#
#     template = loader.get_template('event_manager/login.html')
#     return HttpResponse(template.render({}, request))


def signup_form(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            return redirect('/home/')  # trying to go to login page
    else:
        form = UserCreateForm()
        # Please Add Sign Up form View Here (render, View, 'form':form)
    return render(request, 'event_manager/signup.html', {'form': form})
    pass


def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home/')  # using Login_redirect_url on settings
    else:
        form = AuthenticationForm()
    return render(request, 'event_manager/login.html', {'form': form})
