from django.urls import path
from ventas import views

urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('detalles/', views.detalles, name='detalles'),
]