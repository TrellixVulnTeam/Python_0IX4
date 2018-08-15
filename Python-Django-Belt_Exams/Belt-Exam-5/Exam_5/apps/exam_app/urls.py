from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^show/(?P<user_id>\d+)$', views.show),
    url(r'^join/(?P<user_id>\d+)$', views.join),
    url(r'^poke/(?P<user_id>\d+)$', views.poke),
]