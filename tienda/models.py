from django.db import models
from django.db.models.deletion import CASCADE
from proveedores.models import ArticuloDisponible

# Create your models here.


'''
*******************tercera version******************************

class Producto(ArticuloDisponible):
        
    def save(self, *args, **kwargs):
        # Sobrescribir el método save para establecer siempre inventariado en Tru
        self.inventariado = True
        super().save(*args, **kwargs)

class CategoriaProd(models.Model):
    nombre=models.CharField("Nombre:", max_length=50)
    created=models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated=models.DateTimeField("Fecha de actualización", auto_now_add=True)
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    
    def __str__(self):
        return self.nombre
        
    ******************************segunda version*****************************

class Producto(ArticuloDisponible):
    # Agrega campos específicos de Producto si es necesario
    pvp = models.FloatField("Precio de 1venta", default=0.00)

    def save(self, *args, **kwargs):
        # Calcular el valor de 'pvp' al guardar
        self.pvp = (self.pvd / 70) * 100
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
    
    
    
    *******************primera versión*****************************

class Producto(models.Model):  
    nombre=models.CharField("articulo:", max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=CASCADE, null=True, blank=True)
    
    imagen= models.ImageField(upload_to='media/tienda')
   
    descripcion=models.TextField("descripcion:", max_length=5000)
   
    precio=models.FloatField("precio", default=0.00)
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated=models.DateTimeField("Fecha de actualización", auto_now_add=True)
    
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        
    
    def __str__(self):
        return self.nombre    

    '''