from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.ver_carrito, name='ver'),
    path('agregar/<int:producto_id>/', views.agregar, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminar, name='eliminar'),
    path('vaciar/', views.vaciar, name='vaciar'),
]
