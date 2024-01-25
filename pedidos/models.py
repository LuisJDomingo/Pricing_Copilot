from django.db import models
from django.contrib.auth import get_user_model
# from tienda.models import Producto
from django.db.models import Sum, F, FloatField

from proveedores.models import ArticuloDisponible

# Create your models here.
User=get_user_model()

class Pedido(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']
        
    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.linea_pedido_set.aggregate(
            total=Sum(F('Producto__pvpBigbuy')*F('cantidad'), output_field=FloatField())
        )["total"]
    
class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(ArticuloDisponible, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table = 'linea_pedidos'
        verbose_name = 'linea pedido'
        verbose_name_plural = 'lineas pedidos'