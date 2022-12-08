from django.urls import path
from usuarios import views

urlpatterns=[
    path('usuarios/', views.usuarios, name= 'usuarios'),
    path('datos/', views.datos, name='datos'),
    path('datos/<int:IdUsuario>', views.detalle_datos, name='detalle_datos'),
    path('pagar_cuota/', views.pagar_cuota, name='pagar_cuota'),
    path('cuotas/', views.cuotas, name='cuotas'),
    path('cuotas/<int:IdExpensa>', views.detalle_cuotas, name='detalle_cuotas'),
    path('cuotas/<int:IdExpensa>/pagar', views.pagar_cuota, name='pagar_cuota'),
  
   
    ]