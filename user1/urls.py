from django.urls import path
from django.conf.urls import  include, url
from user1 import views

app_name = 'user1'
urlpatterns = [
    path('', views.index,name='index'),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
	url(r'^register/$', views.register,name='register'),
	url(r'^login/$', views.login,name='login'),
	url(r'^activate/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}'
        r'-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
	
]