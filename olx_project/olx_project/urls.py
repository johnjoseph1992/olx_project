
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views
from olxapp.forms import LoginForm
from rest_framework import routers

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('olxapp.urls')),
    url(r'^$', views.login, {'template_name': 'login.html', 
	'authentication_form': LoginForm, 
	'redirect_authenticated_user': True},name='login'),
    url(r'^logout', views.logout, {'next_page': 'login'}),
   
]


