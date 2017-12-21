from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Member
import requests

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")


    class Meta:
        model = User
        fields = ("first_name","last_name","email","username","password1", "password2")



    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class MemberCreateForm(forms.ModelForm):
    netid=forms.IntegerField(label="Net ID")
    major = forms.CharField(label="Major")

    #need to get user id, which is foreign key, will not save without that

    class Meta:
        model = Member
        fields = ("netid", "major")




