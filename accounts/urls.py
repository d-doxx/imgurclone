from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^user/$', views.UserPage, name='user'),
    url(r'^signup/$', views.SignUp, name='signup'),
    #{'template_name': } is necessary because by default django searches for templates at register/ , we have to rediirect them to our templates
    url(r'^login/$', auth_views.login,{'template_name': 'index.html'},name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'logout.html'},name='logout'),
]