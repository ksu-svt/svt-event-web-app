from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

# Basic Database Schema

class UserProfile(models.Model):
    # A Foreign Key For Users
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    major = models.CharField(max_length=100, default='')
    contact = models.IntegerField(default=0)


# Creates User Profile With User with the post_save Connection
def create_profile(sender, **kwargs):
    # Associates User with user profile
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
