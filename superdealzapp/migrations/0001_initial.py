# Generated by Django 2.1.2 on 2018-10-31 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id_error', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('comentarios', models.CharField(max_length=150)),
                ('url', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id_precio', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=150)),
                ('medida', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, max_length=150, upload_to='productos')),
                ('url', models.URLField(blank=True, max_length=150)),
                ('disponible', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Supermercado',
            fields=[
                ('id_super', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_super', models.CharField(max_length=50)),
                ('main_url', models.URLField(max_length=100)),
                ('term_uso', models.URLField(max_length=150)),
                ('logo', models.CharField(max_length=250)),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='precio',
            name='producto',
            field=models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Producto'),
        ),
        migrations.AddField(
            model_name='precio',
            name='supermercado',
            field=models.ForeignKey(db_column='id_super', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Supermercado'),
        ),
        migrations.AddField(
            model_name='error',
            name='producto',
            field=models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Producto'),
        ),
    ]
