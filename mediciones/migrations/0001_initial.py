# Generated by Django 5.1.2 on 2024-11-25 23:30

import django.db.models.deletion
import django.utils.timezone
import services.utils.GenerarNombre
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fiscalizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentoMedicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('0', 'Luxómetro'), ('1', 'Luminancímetro')], max_length=1, verbose_name='Iipo')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('num_serie', models.CharField(max_length=50, verbose_name='N° de Serie')),
            ],
            options={
                'verbose_name': 'Instrumento de medición',
                'verbose_name_plural': 'Instrumentos de medición',
                'db_table': 'instrumentoMedicion',
            },
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('0', 'Iluminancia'), ('1', 'Luminancia')], max_length=1, verbose_name='Tipo')),
                ('latitud', models.FloatField(verbose_name='Latitud')),
                ('longitud', models.FloatField(verbose_name='Longitud')),
                ('temperatura', models.FloatField(blank=True, null=True, verbose_name='Temperatura (°C)')),
                ('humedad', models.FloatField(blank=True, null=True, verbose_name='Humedad (%)')),
                ('valor_medido', models.FloatField(verbose_name='Valor medido')),
                ('cumplimiento', models.CharField(blank=True, choices=[('0', 'No'), ('1', 'Si')], max_length=1, null=True, verbose_name='Cumplimiento')),
                ('observacion', models.CharField(max_length=500, verbose_name='Observación')),
                ('foto', models.ImageField(default='medicion/medicion.png', null=True, upload_to=services.utils.GenerarNombre.GenerarNombre.generar_nombre_medicion)),
                ('creado', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('fiscalizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiscalizacion.fiscalizacion')),
                ('instrumento_medicion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mediciones.instrumentomedicion')),
            ],
            options={
                'verbose_name': 'Medición',
                'verbose_name_plural': 'Mediciones',
                'db_table': 'medicion',
            },
        ),
    ]
