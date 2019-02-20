from django.forms import ModelForm
from user1.models import User
from django import forms
from django.contrib.auth import authenticate


class UserForm(ModelForm):
    class Meta:
        model=User
        fields = ['lname','fname','email','login','password']
		
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

 
#...
 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
 
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise ValidationError("This field is required.")
        if User.objects.filter(email=self.cleaned_data['email']).count():
            raise ValidationError("Email is taken.")
        return self.cleaned_data['email']
 
    def save(self, request):
 
        user = super(CreateUserForm, self).save(commit=False)
        user.is_active = False
        user.save()
 
        context = {
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'request': request,
            'protocol': request.scheme,
            'username': self.cleaned_data.get('username'),
            'domain': request.META['HTTP_HOST'],
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': default_token_generator.make_token(user),
        }
 
        subject = render_to_string('activation_subject.txt', context)
        email = render_to_string('activation_email.txt', context)
 
        send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email])
 
        return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
		


		
		