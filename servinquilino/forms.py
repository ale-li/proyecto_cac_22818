from django.forms import ModelForm
from msilib.schema import _Validation_records
from wsgiref.validate import validator
from django.forms import ValidationError
from django import forms
from servinquilino.models import Dato, Expensa

def solo_caracteres(valor):
    if any(char.isdigit() for char in valor):
        raise ValidationError('El campo no puede contener números. %(valor)s',
                              code='Error1',
                              params={'valor':valor}
                              )

def solo_numeros(valor):
    pass

class DatosForm(ModelForm):
    class Meta:
        model = Dato
        fields = ['dni', 'nombre', 'apellido', 'calle', 'numero', 'piso', 'dpto', 'observacion']
        #'localidad', 'provincia', 'email',

class ExpensasForm(ModelForm):
    class Meta:
        model = Expensa
        fields = ['anio', 'mes', 'importe', 'fecha']

class DatosForm1(forms.Form):
    dni = forms.CharField(
        label='DNI',
        max_length=8,
        validators=(solo_numeros,),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese DNI'})
        )
    nombre = forms.CharField(
        label='Nombre',
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre'})
        )
    apellido = forms.CharField(
        label='Apellido',
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre'})
        )
    calle = forms.CharField(
        label='Calle',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class':'form-control','placeholder':'Ingrese nombre de la calle'})
        )
    numero = forms.CharField(
        label='Número',
        max_length=5,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese número'})
        )
    piso = forms.CharField(
        label='Piso',
        max_length=2,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese piso'})
        )
    dpto = forms.CharField(
        label='Dpto',
        max_length=3,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese dpto'})
        )
    localidad = forms.CharField(
        label='Localidad',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class':'form-control','placeholder':'Ingrese nombre de la localidad'})
        )
    provincia = forms.CharField(
        label='Provincia',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class':'form-control','placeholder':'Ingrese nombre de la provincia'})
        )
    email = forms.EmailField(
        label='Email',
        max_length=150,
        error_messages={
            'required':'Por favor completa el email'
            },
        widget=forms.TextInput(attrs={'class':'form-control','type':'email'})
        )
    observacion = forms.CharField(
        label='Observaciones',
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':5})
        )

class ExpensasForm1(ModelForm):
    #IdExpensa = models.AutoField(primary_key=True)
    anio = forms.CharField(
        label='Año',
        max_length=4,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Año'})
        )
    mes = forms.CharField(
        label='Mes',
        max_length=4,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Mes'})
        )
    importe = forms.DecimalField(
        label='Importe',
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    pagado = forms.DecimalField(
        label='Pagado',
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    fecha = forms.DateTimeField()

