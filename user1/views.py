from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import User

from django.contrib.auth import authenticate
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


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
            form.save()
            return super(RegisterFormView, self).form_valid(form)
		
from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

