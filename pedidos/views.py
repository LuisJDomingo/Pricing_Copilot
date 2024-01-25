from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
from carro.views import limpiar_carro
from pedidos.models import Pedido, LineaPedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url="/autenticacion/login")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    '''
    *****************************aqui está el error:
                                        IntegrityError at pedidos
                                        FOREIGN KEY constraint failed
                                        Request Method:	GET
                                        Request URL:	http:///127.0.0.1:8000//pedidos//
                                        Django Version:	4.2.7
                                        Exception Type:	IntegrityError
                                        Exception Value:	
                                        FOREIGN KEY constraint failed
                                        
    
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            articulodisponible_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
            
        ))
        
        
    
    
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    
    
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email)
    
    
    messages.success(request, "el pedido se ha realizado con exito")
    
    '''
    
    carro.limpiar_carro()
    
    return redirect("../tienda")


def enviar_mail(**kwargs):
    
    asunto="gracias por comprar"
    mensaje=render_to_string("emails/pedido.html"), {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario"),
        #"emailusuario": kwargs.get("emailusuario")


    }
    
    mensaje_texto=strip_tags(mensaje)
    from_email="luisdomingogarcia79@gmail.com"
    to_mail=kwargs.get("emailusuario")
    
    send_mail(asunto, mensaje_texto, from_email, [to_mail], html_message=mensaje)
    