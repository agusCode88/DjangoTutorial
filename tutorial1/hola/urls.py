from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('',views.hola,name='hola'),
    #path('<str:nombre>/',views.saludo,name='saludo'),
    path('moneda/',views.moneda,name='moneda'),
    path('dragon_ball/',views.dragonBall,name='dragon_ball'),
    path('<str:nombre>/',views.nombreSerie,name='serie')
]
