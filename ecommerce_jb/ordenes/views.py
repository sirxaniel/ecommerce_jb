from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carrito.carrito import Carrito
from .models import Orden, ItemOrden

@login_required
def confirmar_orden(request):
    carrito = Carrito(request)
    if len(carrito) == 0:
        messages.warning(request, 'Tu carrito está vacío.')
        return redirect('carrito:ver')

    if request.method == 'POST':
        orden = Orden.objects.create(usuario=request.user)
        for item in carrito:
            producto = item['producto']
            ItemOrden.objects.create(
                orden=orden,
                producto=producto,
                precio=item['precio'],
                cantidad=item['cantidad'],
            )
            producto.stock -= item['cantidad']
            producto.save()
        carrito.vaciar()
        messages.success(request, f'¡Orden #{orden.id} confirmada!')
        return redirect('ordenes:detalle', pk=orden.id)

    return render(request, 'ordenes/confirmar.html', {'carrito': carrito})

@login_required
def detalle_orden(request, pk):
    orden = get_object_or_404(Orden, pk=pk, usuario=request.user)
    return render(request, 'ordenes/detalle.html', {'orden': orden})

@login_required
def historial(request):
    ordenes = Orden.objects.filter(usuario=request.user)
    return render(request, 'ordenes/historial.html', {'ordenes': ordenes})
