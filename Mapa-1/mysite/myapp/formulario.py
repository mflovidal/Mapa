from django import format
from .models import Marcador

class MarcadorForm(format.ModelForm):
    class Meta:
        model = Marcador
        fields = ['latitud', 'longitud', 'imagen']