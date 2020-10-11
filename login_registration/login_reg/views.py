from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages
# Create your views here.

def index(request):

    return render(request, 'index.html')

def register(request):
    if request.method =="POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pass
            #Create an account