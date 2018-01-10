from django.conf.urls import url

from event_manager.views import EventListView, MemberListView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='home'),
    url(r'^login/$', views.login_form, name='login'),
    url(r'^signup/$', views.signup_form, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^events/$', EventListView.as_view(), name='event-list'),
    url(r'^members/$', MemberListView.as_view(), name='member-list'),
]