from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.http import HttpRequest

class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    netid = models.IntegerField(default=0)
    role = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_full_name()

class Team(models.Model):
    title = models.CharField(max_length=200)
    lead = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(User, related_name="team_members")

    def __str__(self):
        return self.title

class Event(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    dateTime = models.DateTimeField()
    description = models.CharField(max_length=200)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class MemberInline(admin.StackedInline):
    model=Member
    max_num=1

class UserAdmin(AuthUserAdmin):
    inlines=(MemberInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)



# Create your models here.
