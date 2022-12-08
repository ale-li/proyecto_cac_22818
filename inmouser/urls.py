from django.urls import path
from inmouser import views

urlpatterns=[
   
    path('signup/', views.signup, name='signup'),
    path('datos/<int:IdUsuario>/borrar', views.borrar_dato, name='borrar_dato'),
    path('crear_datos/', views.crear_datos, name='crear_datos'),
    path('crear_expensas/', views.crear_expensas, name='crear_expensas'),
    path('cuotas/<int:IdExpensa>/borrar', views.borrar_cuota, name='borrar_cuota'),
    path('logout/', views.signout, name='logout'),
    path('administradores/', views.administradores, name='administradores'),
    ]