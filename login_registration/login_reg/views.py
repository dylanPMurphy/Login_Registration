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
            
            
            # include some logic to validate user input before adding them to the database!
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
            print(pw_hash)      # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
            # be sure you set up your database so it can store password hashes this long (60 characters)
            # make sure you put the hashed password in the database, not the one from the form!
            User.objects.create(name=request.POST['user_name'], password=pw_hash, email=request.POST['email'])
            return redirect('/successRegister') 
            #Create an account

def reg_success(request):
    return render(request, 'successful_REG.html')