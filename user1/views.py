from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from .forms import  LoginForm
from django.contrib.auth import authenticate

from django.contrib import messages

# получение данных из бд
def index(request):
    people = User.objects.all()
    return render(request, "index.html", {"people": people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = User()
        person.name = request.POST.get("name")
        person.email = request.POST.get("email")
        person.login=request.POST.get("login")
        person.lname=request.POST.get("lname")
        person.password=request.POST.get("password")
        person.fname=request.POST.get("fname")
        person.bdate=request.POST.get("bdate")
        person.save()
    return HttpResponseRedirect("/")
 
# изменение данных в бд
def edit(request, id):
    try:
        person = User.objects.get(id=id)
        if request.method == "POST":
            person = User()
            person.name = request.POST.get("name")
            person.email = request.POST.get("email")
            person.login=request.POST.get("login")
            person.lname=request.POST.get("lname")
            person.password=request.POST.get("password")
            person.fname=request.POST.get("fname")
            person.bdate=request.POST.get("bdate")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = User.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
		
#-------------------------------------------------------------Chapter2-registration and Authentication------------
	
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
import datetime
from .forms import  CreateUserForm

#...
app_name = 'user1'
from django.contrib import messages
from  django.shortcuts import redirect
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        f = CreateUserForm(request.POST)
        if f.is_valid():
            f.save(request)
            messages.success(request, 'Account created successfully. Check email to verify the account.')
            return redirect('user1:register')
 
    else:
        f = CreateUserForm()
 
    return render(request, 'register.html', {'form': f})

def login(request):
    if request.method == 'POST':
 
        f = LoginForm(request.POST)
        if f.is_valid():
 
            user = User.objects.filter(email=f.cleaned_data['email'])
 
            if user:
                user = auth.authenticate(
                    username=user[0].username,
                    password=f.cleaned_data['password'],
                )
 
                if user:
                    auth.login(request, user)
                    return redirect( request.GET.get('next') or 'user1:index' )
 
            messages.add_message(request, messages.INFO, 'Invalid email/password.')
            return redirect('user1:login')
 
    else:
        f = LoginForm()
 
    return render(request, 'login.html', {'form': f})




import datetime
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import CreateUserForm

def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if (user is not None and default_token_generator.check_token(user, token)):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.INFO, 'Account activated. Please login.')
    else:
        messages.add_message(request, messages.INFO, 'Link Expired. Contact admin to activate your account.')
 
    return redirect('user1:index')



