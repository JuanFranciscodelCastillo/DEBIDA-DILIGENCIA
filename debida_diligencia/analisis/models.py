# En analisis/models.py
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=10)
    numero_documento = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

# En analisis/models.py
class Informe(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # Otros campos de Informe
