from django.forms import ModelForm
from user1.models import User
from django import forms
from django.contrib.auth import authenticate


class UserForm(ModelForm):
    class Meta:
        model=User
        fields = ['lname','fname','email','login','password']
		

		
		


		
		