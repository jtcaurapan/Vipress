from django import forms
from apps.seminario.models import Seminario
class SeminarioForm(forms.ModelForm):

    class Meta:
        model = Seminario

        fields = [
            'titulo',
            'duracion',
            'Cantidad_participantes',
            'fecha',
            'direccion',
            'orador',
        ]

        labels = {
            'titulo': 'Titulo',
            'duracion': 'Duracion (Horas : Minutos : Segundos)',
            'Cantidad_participantes': 'Cantidad de Participantes',
            'fecha': 'Fecha del Seminario',
            'direccion': 'Ubicación del lugar',
            'orador': 'Oradores',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.TextInput(attrs={'class': 'form-control'}),
            'Cantidad_participantes': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'orador': forms.CheckboxSelectMultiple(),
        }
