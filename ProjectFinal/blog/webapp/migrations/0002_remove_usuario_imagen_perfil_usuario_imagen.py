# Generated by Django 4.1.4 on 2022-12-07 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='imagen_perfil',
        ),
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(max_length=255, null=True, upload_to='categoria/', verbose_name='Imagen'),
        ),
    ]
