from django.urls import path
from django.conf.urls import  include, url
from user1 import views
 
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
	url(r'^register/$', views.RegisterFormView.as_view()),
	url(r'^login/$', views.LoginFormView.as_view()),
]