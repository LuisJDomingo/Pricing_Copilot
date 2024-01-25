from django.db import models

# Create your models here.


class Articulotienda(models.Model):
    
         
    created=models.CharField(("Creado el:"), max_length=50 )
    updated=models.CharField(("Actualizado el:"), max_length=50, null=True)
    
    class Meta:
        verbose_name = 'ctegoria tienda'
        verbose_name_plural = 'categorias tienda'
    
    def __str__(self):
        return (self.nombre)
    
class CategoriaTienda(models.Model):
    
    nombre=models.CharField(max_length=50)
    created=models.CharField(("Creado el:"), max_length=50 )
    updated=models.CharField(("Actualizado el:"), max_length=50, null=True)
    
    class Meta:
        verbose_name = 'ctegoria tienda'
        verbose_name_plural = 'categorias tienda'
    
    def __str__(self):
        return (self.nombre)
    
