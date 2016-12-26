from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^my_board$', views.my_board, name='my_board'),
    url(r'^co_user_1$', views.co_user_1, name='co_user_1'),
    url(r'^co_user_2$', views.co_user_2, name='co_user_2'),

]