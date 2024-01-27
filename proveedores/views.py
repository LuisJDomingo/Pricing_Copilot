from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from proveedores.forms import ImportarCSVForm
from proveedores.models import ArticuloDisponible

from django.http import HttpResponse
import csv
from .models import Articulodisponible

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

def upload_csv(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Archivo no es CSV")
        
        file_data = csv_file.read().decode("utf-8")        
        lines = file_data.split("\n")
        # Omitir el encabezado si lo hay
        for line in lines[1:]:  
            fields = line.split(",")
            # Asegúrate de que la línea no esté vacía
            if line:
                # Crea una instancia de tu modelo
                TuModelo.objects.create(
                    campo1=fields[0],
                    campo2=fields[1],
                    # Asegúrate de asignar todos los campos necesarios
                )
        return HttpResponse("Archivo CSV importado con éxito")
    return HttpResponse("Solicitud inválida")




   
