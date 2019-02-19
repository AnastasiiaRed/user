from django.db import models

class User(models.Model):
    email=models.EmailField(max_length=200)
    login=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    bdate=models.DateTimeField(max_length=200)
    is_blocked=models.BooleanField(max_length=200)
    auth_key=models.CharField(max_length=200)
	