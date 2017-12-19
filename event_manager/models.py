from django.db import models
from django.contrib.auth.models import User

class member(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    last_name=models.CharField(max_length=200)
    netid=models.IntegerField(default=0)
    role=models.CharField(max_length=200)
    major=models.CharField(max_length=200)
    points=models.IntegerField(default=0)

class teams(models.Model):
    user=models.ForeignKey(member,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)

class events(models.Model):
    team=models.ForeignKey(teams,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    dateTime=models.DateTimeField()
    description=models.CharField(max_length=200)
    user=models.ManyToManyField(member)


# Create your models here.
