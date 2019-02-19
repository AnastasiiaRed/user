from django.forms import ModelForm
from user1.models import User
from django import forms

class UserForm(ModelForm):
    class Meta:
        model=User
        fields = ['lname','fname','email','login','password']
		
		