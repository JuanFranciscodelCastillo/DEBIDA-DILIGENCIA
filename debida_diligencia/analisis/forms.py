from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'empresa', 'tipo_documento', 'numero_documento', 'telefono', 'correo']

class DocumentoForm(forms.Form):
    TIPO_DOCUMENTO = [
        ('CC', 'Cedula de Ciudadania'),
        ('CE', 'Cedula de Extranjeria'),
        ('PAS', 'Pasaporte'),
        ('NIT', 'NIT'),
        ('OTRO', 'Otro'),
        # Añadir más tipos de documento según sea necesario
    ]

    tipo_documento = forms.ChoiceField(choices=TIPO_DOCUMENTO)
