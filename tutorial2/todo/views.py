from django.shortcuts import render , redirect
from django.http import request
from .forms import AddForm

# Create your views here.
tareas = []

def home(request):
    context = {'tareas':tareas}
    return render(request,"todo/home.html",context)

def add(request):
    if request.method == 'POST':
        # Si vienen datos en el campo , es POST
        form = AddForm(request.POST)
        if form.is_valid():
            # Nombre del campo en el formulario , la clase del form
            tarea = form.cleaned_data['tarea']
            tareas.append(tarea)
            return redirect('home')
        
    else:
        form = AddForm()
        
    context = {'form':form}    
    return render(request,"todo/add.html",context)