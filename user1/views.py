from django.shortcuts import render
from django.http.response  import HttpResponseRedirect,Http404
from django.template.loader import get_template

from django.shortcuts import render_to_response,redirect,render,get_object_or_404

from user1.models import User
from user1.forms import UserForm
from django.views.decorators.csrf import csrf_protect

from django.contrib import auth

@csrf_protect	
def adduser(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form_valid = form.save(commit=False)        
            form_valid.save()

            return HttpResponseRedirect('/adduser/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'users.html', {'form': form})
