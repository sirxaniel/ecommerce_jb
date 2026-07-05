from django.db import models
from django.contrib.auth.models import User
from tienda.models import Producto

class Orden(models.Model):
    ESTADO_CHOICES = [
        ('pendiente',  'Pendiente'),
        ('procesando', 'Procesando'),
        ('completada', 'Completada'),
        ('cancelada',  'Cancelada'),
    ]
    usuario    = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='ordenes')
    creada     = models.DateTimeField(auto_now_add=True)
    actualizada = models.DateTimeField(auto_now=True)
    estado     = models.CharField(max_length=20,
                                  choices=ESTADO_CHOICES,
                                  default='pendiente')

    class Meta:
        ordering = ['-creada']

    def __str__(self):
        return f'Orden #{self.id} — {self.usuario}'

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items.all())

    def get_total_clp(self):
        return f"${self.get_total():,}".replace(',', '.')


class ItemOrden(models.Model):
    orden    = models.ForeignKey(Orden, on_delete=models.CASCADE,
                                 related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio   = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad}x {self.producto.nombre}'

    def get_subtotal(self):
        return self.precio * self.cantidad

    def get_subtotal_clp(self):
        return f"${self.get_subtotal():,}".replace(',', '.')
