from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Articulo_en_venta
from django.db.models import Sum, F, FloatField


# Create your models here.
User = get_user_model()


class Pedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return (self.lineapedido_set.aggregate(
            total=Sum(F('Producto__pvp')*F('cantidad'),
                      output_field=FloatField())
        )["total"])

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(
        Articulo_en_venta, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio =  models.DecimalField(max_digits=8, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre} a {self.precio}'

    class Meta:
        db_table = 'linea_pedidos'
        verbose_name = 'linea pedido'
        verbose_name_plural = 'lineas pedidos'
        ordering = ['id']


class Factura(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='facturas', null=True)  # Asegúrate de que exista este campo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return (self.lineafactura_set.aggregate(
            total=Sum(F('Producto__pvp')*F('cantidad'),
                      output_field=FloatField())
        )["total"])

    class Meta:
        db_table = 'factura'
        verbose_name = 'factura'
        verbose_name_plural = 'facturas'
        ordering = ['id']

    def __str__(self):
        return f"Factura {self.id} para el Pedido {self.pedido.id}"
    
class LineaFactura(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(
        Articulo_en_venta, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio =  models.DecimalField(max_digits=8, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre} a {self.precio}'

    class Meta:
        db_table = 'linea_factura'
        verbose_name = 'linea factura'
        verbose_name_plural = 'lineas factura'
        ordering = ['id']
