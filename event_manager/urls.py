from django.conf.urls import url
from . import views
# Login Function within Django Framework
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'event_manager/login.html'})
]
