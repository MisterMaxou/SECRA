from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^drop$', views.drop, name="drop"),
    url(r'^edit/(?P<link>[a-zA-Z0-9]{30})$', views.edit, name="edit_work"),
    url(r'^consult/(?P<link>[a-zA-Z0-9]{30})$', views.consult, name='consult'),


]