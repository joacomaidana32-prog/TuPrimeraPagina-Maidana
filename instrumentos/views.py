from django.shortcuts import render, redirect
from .models import Instrumento, Marca, Cliente
from .forms import InstrumentoForm, MarcaForm, ClienteForm, BuscarInstrumentoForm

def inicio(request):
    return render(request, 'instrumentos/inicio.html')

def instrumento_nuevo(request):
    if request.method == "POST":
        form = InstrumentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = InstrumentoForm()
    return render(request, 'instrumentos/instrumento_form.html', {'form': form, 'titulo': 'Cargar Instrumento'})

def marca_nueva(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = MarcaForm()
    return render(request, 'instrumentos/marca_form.html', {'form': form, 'titulo': 'Cargar Marca'})

def cliente_nuevo(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'instrumentos/cliente_form.html', {'form': form, 'titulo': 'Cargar Cliente'})

def buscar_instrumento(request):
    query = request.GET.get('nombre_instrumento', '')
    resultados = []
    if query:
        # Buscamos instrumentos cuyo nombre contenga el texto ingresado
        resultados = Instrumento.objects.filter(nombre__icontains=query)
    
    form = BuscarInstrumentoForm()
    return render(request, 'instrumentos/buscar.html', {
        'form': form, 
        'resultados': resultados, 
        'query': query
    })


