from django.contrib import admin
from .models import ArticuloDisponible

class ArticuloDisponibleAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'preciodemercado')

admin.site.register(ArticuloDisponible, ArticuloDisponibleAdmin)