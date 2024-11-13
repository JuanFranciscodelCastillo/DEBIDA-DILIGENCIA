from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Cliente, Informe

def crear_informe(request):
    # Lógica para crear un informe
    cliente = Cliente.objects.first()
    informe = Informe.objects.create(cliente=cliente, resultado="Informe de Riesgo")
    return JsonResponse({'id': informe.id, 'resultado': informe.resultado})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # home.html es el archivo de plantilla que deseas mostrar

from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo cliente en la base de datos
            return redirect('agregar_cliente')  # Redirige a una página de confirmación
    else:
        form = ClienteForm()
    return render(request, 'home.html', {'form': form})

def home(request):
    return render(request, 'home.html')