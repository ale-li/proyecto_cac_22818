from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth import login

from servinquilino.models import Expensa, Dato

from servinquilino.forms import DatosForm, ExpensasForm


def signin(request):
    if request.method == 'GET':
        return render(request, 'servinquilino/signin.html', {"form": AuthenticationForm})
    else:
        user= authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'servinquilino/signin.html',
                          {"form": AuthenticationForm, "error": "Usuario o Contraseña no válido."})
    login(request, user)
    return redirect('usuarios')



#def login(request):
#    return  render(request, 'servinquilino/login.html')


def nosotros(request):
    return render(request, 'servinquilino/nosotros.html')

def home(request):
    return render(request, 'servinquilino/home.html')


