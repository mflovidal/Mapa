from django import forms
from .models import Sugerencias

class SugerenciaForm(forms.ModelForm):
    class Meta:
        model = Sugerencias
        fields = ["sugerencia"]
        widgets = {'sugerencia': forms.Textarea(attrs={
            'placeholder': 'Escribe tu sugerencia aquí.../Write your suggestion here...', 
            'rows':4
        }),
        }
        labels = {'sugerencia': '',
                  }

from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin']