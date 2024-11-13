# Register your models here.
from django.contrib import admin
from .models import Cliente  # Importa el modelo Cliente

# Define un modelo de administración para Cliente
class ClienteAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de clientes
    list_display = ('nombre', 'empresa', 'tipo_documento', 'numero_documento', 'telefono', 'correo')
    
    # Permite buscar por estos campos en el panel de administración
    search_fields = ('nombre', 'empresa', 'tipo_documento', 'numero_documento', 'telefono', 'correo')
    
    # Filtrar por estos campos en el panel de administración
    list_filter = ('tipo_documento', 'empresa')
    
    # Permite editar varios registros a la vez
    list_editable = ('telefono', 'correo')

# Registra el modelo Cliente con su configuración personalizada
admin.site.register(Cliente, ClienteAdmin)
