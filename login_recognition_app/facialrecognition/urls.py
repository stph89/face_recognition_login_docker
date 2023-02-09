"""Configuración URL de la app

Guardar imagenes en carpeta/localhost redirigir en runserver/ navegacion

--->Documentación para la configuración de URL:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, include
from facialrecognition import views

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('accounts.urls')),
]
