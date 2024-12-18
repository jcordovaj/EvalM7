# Generated by Django 4.2.16 on 2024-11-22 19:20

from django.db import migrations, models
import django.db.models.deletion
import laboratorio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_lab', models.CharField(max_length=255, verbose_name='nombre')),
                ('city_lab', models.CharField(default=None, max_length=255, verbose_name='ciudad')),
                ('pais_lab', models.CharField(default=None, max_length=255, verbose_name='pais')),
                ('creado_lab', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizado_lab', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'Laboratorio',
                'verbose_name_plural': 'Laboratorios',
                'db_table': 'Laboratorio',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_prod', models.CharField(max_length=255, verbose_name='Producto')),
                ('f_fabricacion', models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=laboratorio.models.anio_actual, verbose_name='F Fabricación')),
                ('p_costo', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='P Costo')),
                ('p_venta', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='P Venta')),
                ('creado_prod', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizado_prod', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('lab_prod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='laboratorio.laboratorio')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='DirectorGeneral',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_dire', models.CharField(max_length=255, verbose_name='nombre')),
                ('especialidad', models.CharField(default=None, max_length=255, verbose_name='especialidad')),
                ('creado_dire', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizado_dire', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('lab_dire', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
            options={
                'verbose_name': 'Director General',
                'verbose_name_plural': 'Directores Generales',
                'db_table': 'Director General',
            },
        ),
    ]
