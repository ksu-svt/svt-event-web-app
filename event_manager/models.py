from django.db import models

class Team(models.Model):
    title = models.CharField(max_length=100)

class Event(models.Model):
    title = models.CharField(max_length=100)
    team = models.OneToOneField(Team, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    description = models.CharField(max_length=256)

class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    points = models.IntegerField()
    is_active = models.BooleanField()
    has_paid_dues = models.BooleanField()
    team = models.OneToOneField(Team, null=True, on_delete=models.SET_NULL)
    events = models.ManyToManyField(Event)
