# Generated by Django 3.2.4 on 2021-08-24 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_alter_recorridos_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='mensajeContacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.TextField(verbose_name='Usuario')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('asunto', models.TextField(verbose_name='Asunto')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
                'ordering': ['-created'],
            },
        ),
    ]
