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
def usuarios(request):
    return  render(request, 'usuarios/usuarios.html')


@login_required
def cuotas(request):
    cuotas = Expensa.objects.filter(user=request.user)
    return render(request, 'usuarios/usuarios.html', {"cuotas": cuotas})


@login_required
def cuotas_pagas(request):
    cuotas = Expensa.objects.filter(user=request.user,
                                    fechapago__isnull=False).order_by('-fechapago')
    return render(request, 'usuarios/cuotas.html', {"cuotas": cuotas})

@login_required
def pagar_cuota(request, IdExpensa):
    cuota = get_object_or_404(Expensa, pk=IdExpensa, user=request.user)
    if request.method == 'POST':
        cuota.pagado = cuota.importe
        cuota.fechapago = timezone.now()
        cuota.save()
        return redirect('cuotas')



#@login_required
def detalle_cuotas(request, IdExpensa):
    if request.method == 'GET':
        cuota = get_object_or_404(Expensa, pk=IdExpensa, user=request.user)
        form = ExpensasForm(instance=cuota)
        return render(request, 'usuarios/detalle_cuotas.html', {'cuota': cuota, 'form': form})
    else:
        try:
            cuota = get_object_or_404(Expensa, pk=IdExpensa, user=request.user)
            form = ExpensasForm(request.POST, instance=cuota)
            form.save()
            return redirect('cuotas')
        except ValueError:
            return render(request, 'usuarios/detalle_cuotas.html', {'cuota': cuota, 'form': form, 'error': 'Error actualizando cuota.'})

#@login_required
def datos(request):
    datos = Dato.objects.filter(user=request.user)
    return render(request, 'usuarios/datos.html', {"datos": datos})

#@login_required
def detalle_datos(request, IdUsuario):
    if request.method == 'GET':
        dato = get_object_or_404(Dato, pk=IdUsuario, user=request.user)
        form = DatosForm(instance=dato)
        return render(request, 'usuarios/detalle_datos.html', {'dato': dato, 'form': form})
    else:
        try:
            dato = get_object_or_404(Dato, pk=IdUsuario, user=request.user)
            form = DatosForm(request.POST, instance=dato)
            form.save()
            return redirect('datos')
        except ValueError:
            return render(request, 'usuarios/detalle_datos.html', {'dato': dato, 'form': form, 'error': 'Error actualizando Datos.'})