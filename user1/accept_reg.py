import sys
import os
import django
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.test import Client

django.setup()
csrf_client = Client(enforce_csrf_checks=True)
URL = 'http://127.0.0.1:8080/register'
EMAIL= 'test-user@test.com'
PASSWORD1= 'XXXX'
PASSWORD2='XXXX'
USERNAME= 'test-user'
csrf_client.get(URL) 
csrftoken = csrf_client.cookies['csrftoken']
login_data = dict(email=EMAIL, username=USERNAME,password1=PASSWORD1, password2=PASSWORD2,csrfmiddlewaretoken=csrftoken.value, next='/')
r = csrf_client.post(URL, data=login_data, headers=dict(Referer=URL))