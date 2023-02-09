""" Configuracion de las migraciones para Django:

Clase Migration :
-perfil del username
-imagen
-conexion con la imagen subida"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='null.jpg', upload_to='images'),
        ),
    ]
