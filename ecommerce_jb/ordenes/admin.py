from django.contrib import admin
from .models import Orden, ItemOrden

class ItemOrdenInline(admin.TabularInline):
    model = ItemOrden
    extra = 0
    readonly_fields = ['producto', 'precio', 'cantidad']

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display  = ['id', 'usuario', 'estado', 'get_total_clp', 'creada']
    list_filter   = ['estado']
    list_editable = ['estado']
    inlines       = [ItemOrdenInline]
