from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='home'),
    url(r'^login/$', views.login_form, name='login'),
    url(r'^signup/$', views.signup_form, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^member/$', views.memberRoaster, name='members'),
    url(r'^events/$', views.viewEvent, name='events'),
]