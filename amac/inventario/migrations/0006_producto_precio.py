# Generated by Django 5.1.2 on 2024-12-15 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_rename_proveedor_producto_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(null=True),
        ),
    ]