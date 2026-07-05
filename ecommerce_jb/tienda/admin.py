from django.contrib import admin
from .models import Producto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display   = ['nombre', 'categoria', 'precio_clp', 'stock', 'disponible']
    list_filter    = ['disponible', 'categoria']
    list_editable  = ['disponible', 'stock']
    search_fields  = ['nombre']
    ordering       = ['nombre']
