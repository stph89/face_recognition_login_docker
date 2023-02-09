# Remover descripciones de userprofile

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200324_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
    ]
