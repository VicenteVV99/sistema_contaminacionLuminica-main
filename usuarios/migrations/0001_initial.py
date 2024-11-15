# Generated by Django 5.0.7 on 2024-11-15 18:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'db_table': 'cargo',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Institucion',
                'verbose_name_plural': 'Instituciones',
                'db_table': 'institucion',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=15, verbose_name='Run')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('a_paterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('a_materno', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('correo', models.CharField(max_length=100, verbose_name='Correo')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuarios.cargo')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuarios.institucion')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
    ]
