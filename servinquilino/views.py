from django.shortcuts import render

# Create your views here.



def login(request):
    return  render(request, 'servinquilino/login.html')

def usuarios(request):
    return  render(request, 'servinquilino/usuarios.html')
