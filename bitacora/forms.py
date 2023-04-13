from django.forms import DateTimeInput, ModelForm, TextInput
from bitacora.models import Piloto


class PilotoForm(ModelForm):
    class Meta:
        model = Piloto
        fields = '__all__'  # todas las columnas

        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre',
                    'autocomplete': 'off'
                }
            ),

            'apellido': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido',
                    'autocomplete': 'off'
                }
            ),

            'identificacion': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el cedula',
                    'autocomplete': 'off'
                }
            ),

            'fecha_registro': DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),

            'edad': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido',
                    'autocomplete': 'off'
                }
            ),

            'estado': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido',
                    'autocomplete': 'off'
                }
            ),

            'avatar': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido',
                    'autocomplete': 'off'
                }
            ),

        }
