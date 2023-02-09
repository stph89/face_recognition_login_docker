
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

"""Se crea la Clase Migration:
--> Para correr el programa es necesario correr las migraciones del archivo manage.py 
para inicializar esta app
--> Django hace migraciones automáticas de las tablas, modelos y cualquier
cambio que se efectúe en el framework
--> estas migraciones actualizarán automáticamente la base de datos"""
class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
