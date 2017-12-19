from django.contrib import admin
from .models import Team, Event, Member, UserAdmin
from django.contrib.auth.models import User

admin.site.register(Team)
admin.site.register(Event)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
