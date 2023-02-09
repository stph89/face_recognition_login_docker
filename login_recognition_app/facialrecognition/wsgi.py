"""
Configuración WSGI

 WSGI--> Web Server Gateway InterfaceEs un estandar permite a Django comunicarse a través del protocolo HTTP

Esta configuración queda nombrada en el módulo ``application``.

Mirar la docu:
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

"""Por default se importa de django el parametro env.
 --> es un diccionarion el cual contiene variables wsgi 
relacionadas con la petición del cliente (Método del protocolo, Query String etc ...)"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facialrecognition.settings')

application = get_wsgi_application()
