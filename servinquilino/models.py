#from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import ValidationError

# Create your models here.
# Modelo Datos

class Login(models.Model):
    dni=models.IntegerField(primary_key=True, verbose_name="DNI", null=False, unique=True)
    pasword=models.CharField(max_length=10, verbose_name="Pasword")


class Dato(models.Model):
    IdUsuario = models.AutoField(primary_key=True)
    dni = models.PositiveSmallIntegerField(null=False, unique=True, verbose_name="DNI")
    nombre = models.CharField(max_length=35, null=False, verbose_name="Nombre")
    apellido = models.CharField(max_length=35, null=False, verbose_name="Apellido")
    calle = models.CharField(max_length=100, null=False, verbose_name="Calle")
    numero = models.CharField(max_length=5, null=False, unique=False, verbose_name="Número")
    piso = models.CharField(max_length=2, null=False, unique=False, verbose_name="Piso")
    dpto = models.CharField(max_length=3, null=False, verbose_name="Departamento")
    observacion = models.TextField(
        max_length=200, null=True, blank=True, verbose_name="Observación")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.apellido + ', ' + self.nombre + ', ' + self.user.username


# Modelo Expensas
class Expensa(models.Model):
    IdExpensa = models.AutoField(primary_key=True)
    anio = models.CharField(max_length=4, null=False, unique=False, verbose_name="Año")
    mes = models.CharField(max_length=2, null=False, unique=False, verbose_name="Mes")
    importe = models.DecimalField(max_digits=10, decimal_places=2,
                                  null=False, verbose_name="Importe")
    pagado = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=True, blank=True, verbose_name="Pagado")
    #emision = models.DateTimeField(auto_now_add=True)
    fecha = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="Fecha")
    fechapago = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #IdUsuario = models.ForeignKey(Dato, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        #return str(self.IdExpensa) + ' - ' + self.anio + ' - ' + self.mes + ' $' + str(self.importe)
        return self.user.username + ' - ' + str(self.IdExpensa) + ' - ' + self.anio + ' - ' + self.mes + ' $' + str(self.importe)
