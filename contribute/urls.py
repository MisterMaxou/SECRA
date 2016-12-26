from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.contribute, name="contribute"),
    url(r'^choose_text$', views.choose_text, name="choose_text"),
    url(r'^(?P<link>[a-zA-Z0-9]{30})$', views.edit, name="edit"),
]