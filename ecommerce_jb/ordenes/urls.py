from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('confirmar/', views.confirmar_orden, name='confirmar'),
    path('<int:pk>/',  views.detalle_orden,   name='detalle'),
    path('historial/', views.historial,       name='historial'),
]
