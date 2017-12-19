from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    netid = models.IntegerField(default=0)
    role = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

class Team(models.Model):
    title = models.CharField(max_length=200)
    lead = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(Member, related_name="team_members")

class Event(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    dateTime = models.DateTimeField()
    description = models.CharField(max_length=200)
    user = models.ManyToManyField(Member)


# Create your models here.
