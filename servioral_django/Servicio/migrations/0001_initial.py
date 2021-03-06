# Generated by Django 4.0.4 on 2022-05-10 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False, verbose_name='Id paciente')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('descrip', models.CharField(max_length=500, verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
