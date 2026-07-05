from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('',                              views.catalogo,          name='catalogo'),
    path('producto/<int:pk>/',            views.detalle_producto,  name='detalle'),
    path('buscar/',                       views.buscar,            name='buscar'),
    path('producto/agregar/',             views.agregar_producto,  name='agregar_producto'),
    path('producto/editar/<int:pk>/',     views.editar_producto,   name='editar_producto'),
    path('producto/eliminar/<int:pk>/',   views.eliminar_producto, name='eliminar_producto'),
]
