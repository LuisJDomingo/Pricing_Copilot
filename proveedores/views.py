from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from proveedores.forms import ImportarCSVForm
from proveedores.models import ArticuloDisponible

from django.http import HttpResponse
import csv
from .models import Articulodisponible
import chardet

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

def eliminar_articulo(request, id):
    print(f"ID recibido: {id}")
    articulo = ArticuloDisponible.objects.get(id=id)
    print(f"Antes de la actualización - inventariado: {articulo.inventariado}")
    referencia=articulo.id
    articulo.delete()
    print ("fin")
    return redirect('proveedores')


def importar_csv(request):
    print("empieza la carga")
    if request.method == "POST":
        csv_file = request.FILES['csv_file']  # csv_file: es el nombre del CAMPO en el Formulario Html
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Archivo no es CSV")

        # Detectar la codificación del archivo
        raw_data = csv_file.read()
        encoding = chardet.detect(raw_data)['encoding']
        print(encoding)
        # Decodificar los datos del archivo en la codificación detectada
        file_data = raw_data.decode(encoding)

        reader = csv.reader(file_data.splitlines(), delimiter=',', quotechar='"')
        next(reader, None)  # Omite el encabezado si lo hay
        for i, row in enumerate(reader):
            if i == 1:  # Solo para depuración, imprime la segunda fila
                print(row)
                break
        # Omite el encabezado si lo hay
        for fields in reader:
            if len(fields) < 32:  # Asegúrate de que hay suficientes campos
                continue
            print(len(fields))
            try:
                # Crea una instancia del modelo ArticuloDisponible
                ArticuloDisponible.objects.create(
                    idproveedor=fields[0] if fields[0] else None,
                    categoria=fields[1] if fields[1] else None,
                    nombre=fields[2],
                    atributo1=fields[3] if fields[3] else None,
                    atributo2=fields[4] if fields[4] else None,
                    valor1=fields[5] if fields[5] else None,
                    valor2=fields[6] if fields[6] else None,
                    descripcion=fields[7] if fields[7] else None,
                    marca=fields[8] if fields[8] else None,
                    feature=fields[9] if fields[9] else None,
                    pvpBigbuy=float(fields[10].replace(',', '.')) if fields[10] else None,
                    pvd=float(fields[11].replace(',', '.')) if fields[11] else None,
                    iva=float(fields[12].replace(',', '.')) if fields[12] else None,
                    video=float(fields[13].replace(',', '.')) if fields[13] else None,
                    ean13=fields[14] if fields[14] else None,
                    ancho=float(fields[15].replace(',', '.')) if fields[15] else None,
                    altura=float(fields[16].replace(',', '.')) if fields[16] else None,
                    profundidad=float(fields[17].replace(',', '.')) if fields[17] else None,
                    peso=float(fields[18].replace(',', '.')) if fields[18] else None,
                    stock=int(fields[19]) if fields[19] else 0,
                    imagen1=fields[20] if fields[20] else None,
                    imagen2=fields[21] if fields[21] else None,
                    imagen3=fields[22] if fields[22] else None,
                    imagen4=fields[23] if fields[23] else None,
                    imagen5=fields[24] if fields[24] else None,
                    imagen6=fields[25] if fields[25] else None,
                    imagen7=fields[26] if fields[26] else None,
                    imagen8=fields[27] if fields[27] else None,
                    estado=fields[28] if fields[28] else None,
                    created=fields[29] if fields[29] else None,
                    updated=fields[30] if fields[30] else None,
                    inventariado=fields[31].lower() in ['true', '1', 't', 'y', 'yes', 'sí', 'si'] if fields[31] else False
                )
            except IndexError as e:
                print(f"Error en la línea: {fields}")
                print(f"Mensaje de error: {e}")
                continue  # Continuar con la siguiente línea en caso de error

        return redirect('proveedores')  # Redirige después de procesar todas las líneas
    else:
        return HttpResponse("Solicitud inválida")

def grafico_inventario(request):
    productos = ArticuloDisponible.objects.filter(inventariado=True)
    articulos_en_tienda = len(productos)
    productos = ArticuloDisponible.objects.all()
    productos_por_inventariar= len(productos) - articulos_en_tienda
    
    chart={
        "tooltip": { "trigger": 'item' },
        "legend": { "top": '0%',"left": 'left' },
        "series": [
            {"name": 'Articulos Inventariados',
             "type": 'pie',
             "radius": ['30%', '60%'],
             "avoidLabelOverlap": False,
             "itemStyle": {
                "borderRadius": 10,
                "borderColor": '#fff',
                "borderWidth": 2},
             "label": {
                "show": False,
                "position": 'center'},
             "emphasis": {
                "label": {
                    "show": True,
                    "fontSize": 24,
                    "fontWeight": 'bold'}},
             "labelLine": {
                "show": False
             },
             "data": [
                { "value": articulos_en_tienda, "name": 'Artículos Inventariados'}, #la longitud de la tabala inventario
                { "value": productos_por_inventariar, "name": 'Artículos por Inventariar'}, #la logitud de proveedores meno inventario
                # ejemplo de sintaxis { value: 580, name: 'Email' },
                ]
            }
        ]
        };
    
    return JsonResponse(chart)




   
