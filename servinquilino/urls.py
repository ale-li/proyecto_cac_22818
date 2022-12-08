from django.urls import path
from servinquilino import views

urlpatterns=[
#    path('', views.home, name='home'),
  #    path('', views.login, name= 'login'),
    path('', views.home, name='Home'),
    path('home/', views.home, name='Home'),
    path('nosotros/', views.nosotros , name='nosotros'),
    path('signin/', views.signin, name='signin'),
    
    
        ]
