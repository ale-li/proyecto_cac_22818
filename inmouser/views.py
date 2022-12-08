from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from servinquilino.models import Expensa, Dato

from servinquilino.forms import DatosForm, ExpensasForm



# Create your views here.
def administradores(request):
    return render(request, 'inmonuser/administradores.html')

    

def signup(request):
    if request.method == 'GET':
        return render(request, 'inmonuser/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            
                
            except IntegrityError:
                return render(request, 'servinquilino/home.html', {"form": UserCreationForm, "error": "Usuario ya existe."})
                         
        return render(request, 'inmonuser/signup.html', {"form": UserCreationForm, "error": "Contraseñas no coinciden."})
    
    
    
    
    
@login_required
def signout(request):
    logout(request)
    return redirect('logout')

#@login_required
def crear_datos(request):
    if request.method == "GET":
        return render(request, 'inmonuser/crear_datos.html', {"form": DatosForm})
    else:
        try:
            form = DatosForm(request.POST)
            new_dato = form.save(commit=False)
            new_dato.user = request.user
            new_dato.save()
            return redirect('datos')
        except ValueError:
            return render(request, 'inmonuser/crear_datos.html',
                          {"form": DatosForm, "error": "Error creando Datos Inquilino."})

@login_required
def crear_expensas(request):
    if request.method == "GET":
        return render(request, 'inmonuser/crear_expensas.html', {"form": ExpensasForm})
    else:
        try:
            form = ExpensasForm(request.POST)
            new_expensa = form.save(commit=False)
            new_expensa.user = request.user
            new_expensa.save()
            return redirect('cuotas')
        except ValueError:
            return render(request, 'inmonuser/crear_expensas.html', {"form": ExpensasForm, "error": "Error creando Cuota."})
@login_required
def borrar_dato(request, IdUsuario):
    dato = get_object_or_404(Dato, pk=IdUsuario, user=request.user)
    if request.method == 'POST':
        dato.delete()
        return redirect('datos')
    
@login_required
def borrar_cuota(request, IdExpensa):
    cuota = get_object_or_404(Expensa, pk=IdExpensa, user=request.user)
    if request.method == 'POST':
        cuota.delete()
        return redirect('cuotas')
