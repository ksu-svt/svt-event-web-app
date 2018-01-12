from django.conf.urls import url, include
from django.contrib import admin

from event_manager.views import EventListView, MemberListView, EventDetailView, MemberDetailView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='home'),
    url(r'^login/$', views.login_form, name='login'),
    url(r'^signup/$', views.signup_form, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^events/$', EventListView.as_view(), name='event-list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event-detail'),
    url(r'^members/$', MemberListView.as_view(), name='member-list'),
    url(r'^members/(?P<pk>\d+)/$', MemberDetailView.as_view(), name='member-detail'),
]