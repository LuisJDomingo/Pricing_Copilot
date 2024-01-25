from django.urls import path
from .views import VRegistro, cerrar_sesion, loguear

'''urlpatterns = [
    path('', views.autenticacion, name="autenticacion")'''
    
urlpatterns = [
    path('', VRegistro.as_view(), name="autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('loguear', loguear, name="loguear"),
]
