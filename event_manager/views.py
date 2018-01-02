from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .forms import UserCreateForm,MemberCreateForm
from django.contrib.auth.views import logout as lout
from .models import Member,Event
from datetime import date

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
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreateForm(request.POST)
            member_form = MemberCreateForm(request.POST)
            if form.is_valid() and member_form.is_valid():
                user = form.save()
                member=member_form.save(commit=False)
                member.user=user
                member_form.save()
                return redirect('/home/')
        else:
            form = UserCreateForm()
            member_form = MemberCreateForm()
            # Please Add Sign Up form View Here (render, View, 'form':form)
        return render(request, 'event_manager/signup.html', {'form': form,'member_form':member_form})
    else:
        return redirect('/home/')




def login_form(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('/home/')  # using Login_redirect_url on settings
        else:
            form = AuthenticationForm()
        return render(request, 'event_manager/login.html', {'form': form})
    else:
        return redirect('/home/')

def logout(request):
    lout(request)
    return redirect('/login/')

def memberRoaster(request):
    if request.user.is_authenticated:
        member=Member.objects.all()
        context={'members':member}
        template=loader.get_template('event_manager/members.html')
        return HttpResponse(template.render(context,request))
    else:
        return redirect('/login/')

def viewEvent(request):
    if request.user.is_authenticated:
        dt=date.today()
        event=Event.objects.filter(dateTime__gte=dt)
        context={'events':event}
        template=loader.get_template('event_manager/events.html')
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/login/')