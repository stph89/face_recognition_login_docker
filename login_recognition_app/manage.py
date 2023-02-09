"""Este es el archivo principal para integrar todo el funcionamiento
de Django con el modelo de face_recognition"""

#Importar librerías y paquetes

import os
import sys

"""Línea de comandos de Django para tareas administrativas."""
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facialrecognition.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
             "Instalar Django "
            "Activar entorno virtual e interprete "

        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
