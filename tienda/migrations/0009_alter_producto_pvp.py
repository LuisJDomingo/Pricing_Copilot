# Generated by Django 4.2.7 on 2023-12-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_remove_producto_categorias_remove_producto_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='pvp',
            field=models.FloatField(default=0.0, verbose_name='Precio de 1venta'),
        ),
    ]
