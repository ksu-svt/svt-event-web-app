from django.contrib import admin
from .models import Team, Event, UserAdmin,TeamAdmin,EventAdmin
from django.contrib.auth.models import User

admin.site.register(Team,TeamAdmin)
admin.site.register(Event,EventAdmin)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
