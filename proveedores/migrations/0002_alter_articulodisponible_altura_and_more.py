# Generated by Django 4.2.7 on 2023-11-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulodisponible',
            name='altura',
            field=models.FloatField(verbose_name='Alto'),
        ),
        migrations.AlterField(
            model_name='articulodisponible',
            name='ancho',
            field=models.FloatField(verbose_name='Ancho'),
        ),
        migrations.AlterField(
            model_name='articulodisponible',
            name='profundidad',
            field=models.FloatField(verbose_name='Profundo'),
        ),
    ]
