# Control de migraciones

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_userprofile_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='null.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.CharField(default='NULL USER', max_length=25),
        ),
    ]
