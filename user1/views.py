from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import User
 
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
	

