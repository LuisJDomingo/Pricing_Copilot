from django.db import models
import random
from requests_html import HTMLSession
from bs4 import BeautifulSoup 

# Create your models here.
from django.db import models

class ArticuloDisponible(models.Model):
    '''
    categoria = models.CharField(("Categoria"), max_length=50, null=True, blank=True)    
    '''
    nombre = models.CharField(("Nombre"), max_length=50)
    
    atributo1 = models.CharField(("Atributo 1"), max_length=50, null=True, blank=True)
    atributo2 = models.CharField(("Atributo 2"), max_length=50, null=True, blank=True)
    valor1 = models.CharField((" Valor 1"), max_length=50, null=True, blank=True)
    valor2 = models.CharField(("Valor 2"), max_length=50, null=True, blank=True)
    descripcion = models.CharField(("Descripción"), max_length=500, null=True, blank=True)
    marca = models.CharField(("Marca"), max_length=50, null=True, blank=True)
    feature = models.CharField(("Feature"), max_length=50, null=True, blank=True)
    pvpBigbuy = models.FloatField(("PVP venta al publico en Bigbuy"))
    pvd = models.FloatField(("Precio en Origen"), null=True, blank=True)
    iva = models.FloatField(("I.V.A."), null=True, blank=True)
    video = models.FloatField(("Video"), null=True, blank=True)
      
    ean13 = models.CharField(("ean"), max_length=50, null=True, blank=True)
    ancho = models.FloatField(("Ancho"), null=True, blank=True)
    altura = models.FloatField(("Alto"), null=True, blank=True)
    profundidad = models.FloatField(("Profundo"), null=True, blank=True)
    peso = models.FloatField(("Peso"), null=True, blank=True)
    stock = models.IntegerField(("Stock"), default=0)
    imagen1 = models.URLField(("Imágen"), max_length=5000, null=True, blank=True)
    imagen2 = models.URLField(("Imágen"), max_length=500, null=True, blank=True)
    imagen3 = models.URLField(("Imágen"), max_length=500, null=True, blank=True)
    imagen4 = models.URLField(("Imágen"), max_length=500, null=True, blank=True)
    imagen5 = models.URLField(("Imágen"), max_length=500, null=True, blank=True)
    imagen6 = models.URLField(("Imágen"), max_length=500, null=True, blank=True)
    imagen7 = models.URLField(("Imágen"), max_length=500, null=True, blank=True)
    imagen8 = models.URLField(("Imágen"), max_length=500, null=True, blank=True)
    estado = models.CharField(("Estado:"), max_length=50, null=True, blank=True)
    created = models.CharField(("Creado el:"), max_length=50, null=True)
    updated = models.CharField(("Actualizado el:"), max_length=50, null=True)
    inventariado = models.BooleanField(("Inventariado"), default=False)
    preciodemercado = models.FloatField(("Precio de Mercado"), default=0, null=True)

    def save(self, *args, **kwargs):
        # Actualizar el atributo 'preciodemercado' al guardar
        random_offset = random.uniform(-10, 10)
        self.preciodemercado = round(float(self.pvpBigbuy) + random_offset, 2)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Articulo disponible para la venta en proveedores'
        verbose_name_plural = 'Articulos disponibles para la venta en proveedores'
    
    def __str__(self):
        return (self.nombre)
    
    def precio_de_mercado(self, *args, **kwargs):
        session = HTMLSession()
        s
        pass
        
