from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Cliente, Informe

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Empresa X", direccion="123 Calle")

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nombre, "Empresa X")
        self.assertEqual(self.cliente.direccion, "123 Calle")

from django.test import TestCase
from django.urls import reverse
from .models import Cliente, Informe

class CrearInformeViewTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Empresa X", direccion="123 Calle")

    def test_crear_informe(self):
        response = self.client.get(reverse('crear_informe'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('resultado', response.json())
