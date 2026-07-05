JB Store - E-Commerce Django
=============================

Aplicacion web de e-commerce desarrollada en Django como proyecto
de portafolio profesional. Permite gestionar productos, categorias,
carrito de compras y ordenes con un diseno moderno y responsivo.


FUNCIONALIDADES
---------------

Cliente:
- Catalogo con filtro por categorias
- Buscador de productos
- Carrito de compras con sesion
- Confirmacion e historial de ordenes
- Registro, login y logout

Administrador:
- Agregar productos con foto desde el catalogo
- Editar productos existentes
- Eliminar productos con confirmacion
- Control de stock automatico
- Gestion de categorias desde panel admin


TECNOLOGIAS
-----------

- Python 3.x        Lenguaje principal
- Django 6.0        Framework web
- SQLite            Base de datos
- Bootstrap 5.3     Diseno y UI
- Pillow            Manejo de imagenes


INSTALACION
-----------

1. Crear entorno virtual
   python -m venv venv
   venv\Scripts\activate

2. Instalar dependencias
   pip install -r requirements.txt

3. Aplicar migraciones
   python manage.py migrate

4. Crear superusuario
   python manage.py createsuperuser

5. Ejecutar servidor
   python manage.py runserver

Abrir en: http://127.0.0.1:8000


ESTRUCTURA DEL PROYECTO
------------------------

ecommerce_jb/
├── ecommerce/       Configuracion principal
├── tienda/          App productos y catalogo
├── carrito/         App carrito (sesion)
├── ordenes/         App ordenes
├── usuarios/        App autenticacion
├── templates/       Templates HTML
├── media/           Imagenes subidas
└── static/          Archivos estaticos


AUTOR
-----

Daniel Navarrete C.
Proyecto Portafolio - Modulo 8 Django
