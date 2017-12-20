from django.shortcuts import render, redirect
# Signup Authentication
from django.contrib.auth.forms imports UserCreationForm, AuthenticationForm
# Login Function within Django Framework
from django.contrib.auth.views import login


def home(request):
    return render(request, 'event_manager/home.html')


def signup_form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            return redirect('/home/')  # trying to go to login page
    else:
        form = UserCreationForm()
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
