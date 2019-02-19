
import datetime
from django.db import models
from django.utils import timezone
class User(models.Model):
    email=models.EmailField(max_length=200)
    login=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    bdate=models.DateTimeField(max_length=200,null=True)
    is_blocked=models.BooleanField(max_length=200,null=True)
    auth_key=models.CharField(max_length=20,default='123456')
	