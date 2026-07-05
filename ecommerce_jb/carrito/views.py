from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from tienda.models import Producto
from .carrito import Carrito

def ver_carrito(request):
    carrito = Carrito(request)
    return render(request, 'carrito/carrito.html', {'carrito': carrito})

def agregar(request, producto_id):
    carrito  = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id, disponible=True)
    try:
        cantidad = int(request.POST.get('cantidad', 1))
        carrito.agregar(producto, cantidad=cantidad)
        messages.success(request, f'"{producto.nombre}" agregado al carrito.')
    except ValueError as e:
        messages.error(request, str(e))
    return redirect('carrito:ver')

def eliminar(request, producto_id):
    carrito  = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    messages.info(request, f'"{producto.nombre}" eliminado del carrito.')
    return redirect('carrito:ver')

def vaciar(request):
    carrito = Carrito(request)
    carrito.vaciar()
    messages.info(request, 'Carrito vaciado.')
    return redirect('carrito:ver')
