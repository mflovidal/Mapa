from django.urls import path
from . import views


urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('myapp/', views.myapp, name='myapp'),
    path('', views.calendario_view, name='calendario'),
    path('editar_evento/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('editar_evento/', views.editar_evento, name='editar_evento_nuevo'),
    ]

