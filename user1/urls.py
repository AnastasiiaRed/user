from django.urls import path
from django.conf.urls import  include, url
from user1 import views
from django.contrib.auth import views as auth_views

app_name = 'user1'
urlpatterns = [
    path('', views.index,name='index'),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
	path('calc_age/<int:id>/', views.calc_age),
	path('get_FIO/<int:id>/', views.get_FIO),
    path('delete/<int:id>/', views.delete),
	url(r'^register/$', views.register,name='register'),
	url('login/$', views.login,name='login'),
	url(r'^activate/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}'
        r'-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
  url('^password-reset/$', auth_views.PasswordResetView.as_view(),
        {'template_name': 'djangobin/password_reset.html',
         'email_template_name': 'djangobin/email/password_reset_email.txt',
         'subject_template_name': 'djangobin/email/password_reset_subject.txt',
         'post_reset_redirect': 'djangobin:password_reset_done',
        },
        name='password_reset'),
 
    url('^password-reset-done/$', auth_views.PasswordResetDoneView.as_view(),
        {'template_name': 'djangobin/password_reset_done.html',},
        name='password_reset_done'),
 
    url(r'^password-confirm/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}'
        r'-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        {'template_name': 'djangobin/password_reset_confirm.html',
         'post_reset_redirect': 'djangobin:password_reset_complete'},
        name='password_reset_confirm'),
 
    url(r'password-reset-complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        {'template_name':
             'djangobin/password_reset_complete.html'},
        name='password_reset_complete'),
    ]