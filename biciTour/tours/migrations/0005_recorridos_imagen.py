# Generated by Django 3.2.4 on 2021-08-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_registrorecorrido'),
    ]

    operations = [
        migrations.AddField(
            model_name='recorridos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Imagen recorrido'),
        ),
    ]
