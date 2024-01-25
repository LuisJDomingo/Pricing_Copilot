from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from proveedores.forms import ImportarCSVForm
from proveedores.models import ArticuloDisponible

@login_required(login_url="/autenticacion/loguear")
def proveedores(request, articulo_id=None):
    articulosproveedores = ArticuloDisponible.objects.all()
    
    return render(request, 'proveedores/proveedores.html', 
                  {"articulosproveedores": articulosproveedores})
    

    
def guardar_manualmente(request):
    nombre=request.POST['txtnombre']
    pvpBigbuy=request.POST['numprecio']
    ean13=request.POST['ean13']
    imagen1=request.POST['imagen1']
    
    articulo=ArticuloDisponible.objects.create(nombre=nombre, pvpBigbuy=pvpBigbuy, ean13=ean13, imagen1=imagen1)
    return redirect('proveedores')

def inventariar(request, id):
    print(f"ID recibido: {id}")
    articulo = ArticuloDisponible.objects.get(id=id)
    print(f"Antes de la actualización - inventariado: {articulo.inventariado}")
    articulo.inventariado = not articulo.inventariado
    articulo.save()
    print(f"Después de la actualización - inventariado: {articulo.inventariado}")
    return redirect('proveedores')
