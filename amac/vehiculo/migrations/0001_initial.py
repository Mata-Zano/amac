# Generated by Django 5.1.2 on 2024-11-19 23:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais_origen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('tipo', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('motor', models.CharField(max_length=100)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelos', to='vehiculo.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('anio_fabricacion', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('Kilometraje', models.IntegerField()),
                ('patente', models.CharField(max_length=10)),
                ('num_chasis', models.CharField(max_length=50)),
                ('num_motor', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculo.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculo.modelo')),
            ],
        ),
    ]
