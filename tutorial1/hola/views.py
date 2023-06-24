from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def hola(request):
    return render(request,'hola/index.html')

def saludo(request,nombre):
    context = {'name':nombre}
    return render(request,'hola/saludo.html',context)

def moneda(request):
    num = 1
    context = {'num':num}
    return render(request,'hola/moneda.html',context)

def dragonBall(request):
        return HttpResponse("Dragon Ball")
    
def nombreSerie(request,nombre):
    return HttpResponse(f"Nombre Serie: {nombre}")