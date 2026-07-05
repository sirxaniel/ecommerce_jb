from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db.models import Q
from .models import Producto, Categoria
from .forms import ProductoForm

def solo_staff(user):
    return user.is_staff

def catalogo(request):
    productos  = Producto.objects.filter(disponible=True).select_related('categoria')
    categorias = Categoria.objects.all()
    categoria_slug   = request.GET.get('categoria')
    categoria_activa = None

    if categoria_slug:
        categoria_activa = get_object_or_404(Categoria, slug=categoria_slug)
        productos = productos.filter(categoria=categoria_activa)

    return render(request, 'tienda/catalogo.html', {
        'productos':         productos,
        'categorias':        categorias,
        'categoria_activa':  categoria_activa,
        'form':              ProductoForm(),
    })

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, disponible=True)
    return render(request, 'tienda/detalle.html', {'producto': producto})

def buscar(request):
    query     = request.GET.get('q', '')
    productos = []
    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) |
            Q(categoria__nombre__icontains=query),
            disponible=True
        ).distinct()
    return render(request, 'tienda/buscar.html', {
        'productos': productos,
        'query':     query,
    })

@user_passes_test(solo_staff, login_url='/usuarios/login/')
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Producto agregado correctamente!')
        else:
            messages.error(request, 'Error al agregar. Revisa los campos.')
    return redirect('tienda:catalogo')

@user_passes_test(solo_staff, login_url='/usuarios/login/')
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{producto.nombre}" actualizado.')
            return redirect('tienda:catalogo')
        else:
            messages.error(request, 'Error al actualizar. Revisa los campos.')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/editar_producto.html', {
        'form':     form,
        'producto': producto,
    })

@user_passes_test(solo_staff, login_url='/usuarios/login/')
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.info(request, f'"{nombre}" eliminado correctamente.')
        return redirect('tienda:catalogo')
    return render(request, 'tienda/confirmar_eliminar.html', {'producto': producto})
