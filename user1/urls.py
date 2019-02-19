from django.contrib import admin
from . import views

from django.conf.urls import include, url


urlpatterns=[
		url(r'',views.adduser,name='adduser'),

]
