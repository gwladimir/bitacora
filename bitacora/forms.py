from django.forms import ModelForm, TextInput, Textarea
from bitacora.models import Piloto


class PilotoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Piloto
        fields = '__all__'  # todas las columnas
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre',

                }
            ),

            'apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese el apellido',
                }
            ),

            'identificacion': TextInput(
                attrs={
                    'placeholder': 'Ingrese la cedula',
                }
            ),

            'edad': TextInput(
                attrs={
                    'placeholder': 'Ingrese el apellido',
                }
            ),

            'estado': TextInput(
                attrs={
                    'placeholder': 'Ingrese el apellido',
                }
            ),

            'avatar': TextInput(
                attrs={
                    'placeholder': 'Ingrese el apellido',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
