# Automigraciones

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='null.jpg', upload_to='images'),
        ),
    ]
