from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
    
class Categoria(models.Model):
    nombre=models.CharField("Nombre:", max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    
    titulo=models.CharField("Título:", max_length=50)
    contenido=models.TextField("Entrada:", max_length=50)
    imagen=models.ImageField(upload_to='media/blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Entrada'
        verbose_name_plural='Entradas'
        
    
    def __str__(self):
        return self.titulo
    
    
    

    