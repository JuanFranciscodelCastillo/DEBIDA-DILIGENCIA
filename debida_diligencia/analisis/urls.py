from django.urls import path
from . import views

urlpatterns = [
   path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
   path('', views.home, name='home'),  # Establece la vista para la ruta raíz
]

