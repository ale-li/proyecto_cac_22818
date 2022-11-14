from django.urls import path
from servinquilino.views import   login, usuarios




urlpatterns=[    

    path('', login, name= 'login'),
    path('usuarios', usuarios, name= 'usuarios'),
     
]


