
from django.contrib import admin
from .models import Sugerencias


@admin.register(Sugerencias)
class SugerenciasAdmin(admin.ModelAdmin):
    list_display = ('sugerencia', 'fecha_creacion')  
    ordering = ('-fecha_creacion',)  
    search_fields = ('sugerencia',)  




