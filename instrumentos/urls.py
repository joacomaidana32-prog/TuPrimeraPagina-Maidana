from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('instrumento/nuevo/', views.instrumento_nuevo, name='instrumento_nuevo'),
    path('marca/nueva/', views.marca_nueva, name='marca_nueva'),
    path('cliente/nuevo/', views.cliente_nuevo, name='cliente_nuevo'),
    path('buscar/', views.buscar_instrumento, name='buscar'),
]