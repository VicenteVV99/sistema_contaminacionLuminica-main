# Generated by Django 5.0.7 on 2024-11-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_mediciones', '0012_medicion_creado'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicion',
            name='estado',
            field=models.IntegerField(default=0),
        ),
    ]
