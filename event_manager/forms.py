from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Member

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")

    #validate email
    #active status? set by admin??

    class Meta:
        model = User
        fields = ("first_name","last_name","email","username","password1", "password2")



    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class MemberCreateForm(forms.ModelForm):
    netid=forms.IntegerField(label="Net ID")
    major = forms.CharField(label="Major")

    class Meta:
        model = Member
        fields = ("netid", "major")

    def save(self, commit=True):
        user=super(MemberCreateForm,self).save(commit=False)
        Member.netid=self.cleaned_data["netid"]
        Member.major=self.cleaned_data["major"]

        if commit:
            user.save()
        return user


