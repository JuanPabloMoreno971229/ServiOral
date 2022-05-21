# Generated by Django 4.0.4 on 2022-05-10 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Documento', '0001_initial'),
        ('Ciudad', '0001_initial'),
        ('Genero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False, verbose_name='Id paciente')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('phone', models.IntegerField(verbose_name='Número de teléfono')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo electronico')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ciudad.ciudad')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Documento.documento')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Genero.genero')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]
