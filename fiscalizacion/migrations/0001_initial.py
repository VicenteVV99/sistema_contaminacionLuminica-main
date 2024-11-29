# Generated by Django 5.1.3 on 2024-11-28 16:26

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyectos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiscalizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='proyectos.proyecto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fiscalización',
                'verbose_name_plural': 'Fiscalizaciones',
                'db_table': 'fiscalizacion',
            },
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('fiscalizacion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fiscalizacion.fiscalizacion')),
            ],
            options={
                'verbose_name': 'Reporte',
                'verbose_name_plural': 'Reportes',
                'db_table': 'reporte',
            },
        ),
    ]
