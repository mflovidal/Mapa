from django.urls import path
from . import views
from .views import obtener_mensaje, casa

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('myapp/', views.myapp, name='myapp'),
    #marcador /agregar_marcador, editar_marcador/
    #path('agregar/', agregar_marcador, name='agregar_marcador'),
    #path('editar/', editar_marcador, name='editar_marcador'),
    # mensaje
    path('obtener-mensaje/',obtener_mensaje, name='mapa'),
    path('', casa, name='casa')
]