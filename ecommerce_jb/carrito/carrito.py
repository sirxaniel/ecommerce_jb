from tienda.models import Producto

CARRITO_SESSION_KEY = 'carrito'

class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get(CARRITO_SESSION_KEY)
        if not carrito:
            carrito = self.session[CARRITO_SESSION_KEY] = {}
        self.carrito = carrito

    def agregar(self, producto, cantidad=1):
        pid = str(producto.id)
        if pid not in self.carrito:
            self.carrito[pid] = {'cantidad': 0, 'precio': producto.precio}
        nueva_cantidad = self.carrito[pid]['cantidad'] + cantidad
        if nueva_cantidad > producto.stock:
            raise ValueError(f'Stock insuficiente. Disponible: {producto.stock}')
        self.carrito[pid]['cantidad'] = nueva_cantidad
        self.guardar()

    def eliminar(self, producto):
        pid = str(producto.id)
        if pid in self.carrito:
            del self.carrito[pid]
            self.guardar()

    def guardar(self):
        self.session.modified = True

    def vaciar(self):
        del self.session[CARRITO_SESSION_KEY]
        self.guardar()

    def get_total(self):
        return sum(item['precio'] * item['cantidad']
                   for item in self.carrito.values())

    def get_total_clp(self):
        return f"${self.get_total():,}".replace(',', '.')

    def __iter__(self):
        ids      = self.carrito.keys()
        productos = Producto.objects.filter(id__in=ids)
        carrito  = self.carrito.copy()
        for p in productos:
            carrito[str(p.id)]['producto'] = p
        for item in carrito.values():
            item['subtotal']     = item['precio'] * item['cantidad']
            item['subtotal_clp'] = f"${item['subtotal']:,}".replace(',', '.')
            item['precio_clp']   = f"${item['precio']:,}".replace(',', '.')
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.carrito.values())
