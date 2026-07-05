from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug   = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre      = models.CharField(max_length=200)
    categoria   = models.ForeignKey(Categoria, on_delete=models.SET_NULL,
                                    null=True, related_name='productos')
    descripcion = models.TextField(blank=True)
    precio      = models.PositiveIntegerField(help_text='Precio en CLP sin puntos')
    stock       = models.PositiveIntegerField(default=10)
    imagen      = models.ImageField(upload_to='productos/', blank=True, null=True)
    disponible  = models.BooleanField(default=True)
    creado      = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    @property
    def precio_clp(self):
        return f"${self.precio:,}".replace(',', '.')

    @property
    def hay_stock(self):
        return self.stock > 0
