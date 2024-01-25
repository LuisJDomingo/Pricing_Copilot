# Generated by Django 4.2.7 on 2023-11-21 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_alter_articuloenventa_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre:')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='articulo:')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media/tienda')),
                ('descripcion', models.TextField(max_length=5000, verbose_name='descripcion:')),
                ('precio', models.FloatField(default=0.0, verbose_name='precio')),
                ('disponibilidad', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categorias', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.categoriaprod')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.DeleteModel(
            name='ArticuloenVenta',
        ),
        migrations.DeleteModel(
            name='Categoriaarticuloenventa',
        ),
    ]