from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic import ListView

from .forms import UserCreateForm,MemberCreateForm
from django.contrib.auth.views import logout as lout

from event_manager.models import Event, Member


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class MemberListView(LoginRequiredMixin, ListView):
    model = Member
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def index(request):
    template=loader.get_template('event_manager/index.html')
    return HttpResponse(template.render({}, request))

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
