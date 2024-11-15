from django.urls import path
from . import views


urlpatterns = [
    path('', views.myapp, name='myapp'),
    #path('myapp/', views.myapp, name='myapp'), creo que no hace nada 'creo'
    path('view/', views.view_calendar, name='view_calendar'),
    path('edit/', views.edit_calendar, name='edit_calendar'),
    #path('login/', views.login_view, name='login'),
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/', views.update_event, name='update_event'),
    path('delete_event/', views.delete_event, name='delete_event'),
    ]

