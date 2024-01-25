from django.shortcuts import render, HttpResponse
from carro.carro import Carro
from proveedores.models import ArticuloDisponible
# Create your views here.
def home(request):
    carro=Carro(request)
    return render(request,'proyectoweb_app/home.html')

def inventario(request):
    return render(request,'proyectoweb_app/inventario.html')