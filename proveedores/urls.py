from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
from autenticacion.views import loguear


urlpatterns = [
    path('', views.proveedores, name='proveedores'),
    path('guardar_manualmente/', views.guardar_manualmente, name='guardar_manualmente'),
    path('inventariar/<int:id>', views.inventariar, name='inventariar'),
    
    path('autenticacion/login/', LoginView.as_view(), name='login'),
    
    
]


