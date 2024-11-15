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
class CustomLoginForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=100)
    clave_secreta = forms.CharField(widget=forms.PasswordInput)
