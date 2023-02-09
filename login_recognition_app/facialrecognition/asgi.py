"""
--> Configuración ASGI para nuestra app de login por reconocimiento facial.

--> la llamada ASGI se configura como una variable a nivel de módulo llamada ``application``.

--> Consultar la docu de Django:
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facialrecognition.settings')

application = get_asgi_application()
