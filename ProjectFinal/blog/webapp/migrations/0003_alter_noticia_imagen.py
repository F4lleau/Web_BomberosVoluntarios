# Generated by Django 4.1.4 on 2022-12-11 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_usuario_imagen_perfil_usuario_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(max_length=255, null=True, upload_to='categoria/', verbose_name='Imagen'),
        ),
    ]
