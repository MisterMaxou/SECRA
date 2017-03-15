"""oeno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from nosbrouillons import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import tinymce



urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^work/', include('work.urls')),
    url(r'^aboutus/', include('aboutus.urls')),
    url(r'^account/', include('account.urls')),
    # url(r'^news/', include('news.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^contribute/', include('contribute.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('main.urls')),
    # url(r'^xmpp/', include("xmpp.urls")),
]

urlpatterns += staticfiles_urlpatterns()


handler404 = 'main.views.not_found_error'

