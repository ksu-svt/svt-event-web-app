from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Member

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    netid=forms.IntegerField(label="Net ID")
    major = forms.CharField(label="Major")

    class Meta:
        model = User
        fields = ("first_name","last_name","email","netid","major","username","password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user