from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
from carro.views import limpiar_carro
from pedidos.models import Pedido, LineaPedido, Factura, LineaFactura
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from tienda.models import Articulo_en_venta


# Create your views here.

@login_required(login_url="/autenticacion/login")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    
    print("contenido del carro: ", carro.carro)
                           
    for key, value in carro.carro.items():
        producto = Articulo_en_venta.objects.get(id=key)  # Obtiene el producto
        precio = producto.precio  # Obtiene el precio del producto
        linea = LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido,
            precio=precio  # Usa el precio obtenido
        )
        lineas_pedido.append(linea)
        
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email)
    
    messages.success(request, "el pedido se ha realizado con exito") 
    
    generar_factura(request, pedido)
    
    carro.limpiar_carro()
    
    return redirect("../tienda")


def enviar_mail(pedido, lineas_pedido, nombreusuario, emailusuario):

    asunto = "Gracias por comprar"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": pedido,
        "lineas_pedido": lineas_pedido,
        "nombreusuario": nombreusuario,
    })
    mensaje_texto = strip_tags(mensaje)
    from_email = "luisdomingo@cosasmolonas.eu"
    to_mail = emailusuario  # Utilizar el email proporcionado en los argumentos
    
    print(mensaje_texto)

    print("Hasta aquí todo bien, se crea el mail")

    send_mail(asunto, mensaje_texto, from_email, [to_mail], html_message=mensaje)
    
    print("Hasta aquí todo bien, se envía el mail")

def generar_factura(request, pedido):
    factura=Factura.objects.create(user=request.user, pedido=pedido)
    carro=Carro(request)
    lineas_factura=list()
    
    print("contenido del carro: ", carro.carro )
    
    print("esto lo hace")                   
    for key, value in carro.carro.items():
        print(key, value)
        producto = Articulo_en_venta.objects.get(id=key)  # Obtiene el producto
        precio = producto.precio  # Obtiene el precio del producto
        linea = LineaFactura(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido,
            precio=precio  # Usa el precio obtenido
        )
        lineas_factura.append(linea)
        for linea in lineas_factura:
            print(linea, "1")
        print("esto lo hace 2")                   

    LineaFactura.objects.bulk_create(lineas_factura)
    print("esto lo hace 3")                   

    '''
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email)
    '''
    messages.success(request, "la factura se ha realizado con exito") 
