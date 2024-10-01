from django.urls import path
from .views import home, CrearMensaje,EliminarMensaje,MensajesRecibidos

urlpatterns = [
    path('', home, name='home'),
    path('enviar/', CrearMensaje.as_view(), name='enviar_mensaje'),
    path('recibidos/', MensajesRecibidos.as_view(), name='mensajes_recibidos'),
    path('eliminar/<int:pk>', EliminarMensaje.as_view(), name='eliminar_mensaje'),
]