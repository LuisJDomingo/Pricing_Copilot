# Generated by Django 4.2.7 on 2023-12-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_categoriaprod_producto_delete_articuloenventa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='media/tienda'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización'),
        ),
    ]