# Generated by Django 5.0.4 on 2024-05-08 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('plate', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='Patente')),
                ('brand', models.CharField(max_length=50, verbose_name='Marca')),
                ('model', models.CharField(max_length=50, verbose_name='Modelo')),
                ('year', models.IntegerField(verbose_name='Año')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='RUT')),
                ('fname', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lname', models.CharField(max_length=50, verbose_name='Apellido')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehicle', verbose_name='Vehículo')),
            ],
        ),
        migrations.CreateModel(
            name='AccountingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_date', models.DateTimeField(verbose_name='Fecha de compra')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehicle', verbose_name='Vehículo')),
            ],
        ),
    ]
