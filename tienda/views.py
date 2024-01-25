from django.shortcuts import render
from proveedores.models import ArticuloDisponible


# Create your views here.
def tienda(request):
    inventario=[]
    productos = ArticuloDisponible.objects.filter(inventariado=True)
    for producto in productos:
        if producto.inventariado==True:
            inventario.append(producto)
    return render(request,'tienda/tienda.html', {"inventario": inventario})