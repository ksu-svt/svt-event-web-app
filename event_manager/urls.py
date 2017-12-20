from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', views.login_form, {'template_name': 'event_manager/login.html'})
    url(r'^signup/$', views.signup_form, {'template_name': 'event_manager/signup.html'})
]
