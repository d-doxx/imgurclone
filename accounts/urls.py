from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^user/$', views.UserPage, name='user'),
    url(r'^signup/$', views.SignUp, name='signup'),
    # {'template_name': } is necessary because by default django searches for templates at register/ , we have to rediirect them to our templates
    url(r'^signin/$', views.HomePage,name='signin'),
    url(r'^login/$', auth_views.login,name='login'),
    # sigin and login urls are different, to sign in the website, go to /signin 
    # the login url only performs function of logging in using the inbuilt django functions, but it does not have a proper user interface 
    url(r'^logout/$', auth_views.logout,{'next_page': 'Home'},name='logout'),
]