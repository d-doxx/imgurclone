from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'base.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'base.html'},name='logout'),
]