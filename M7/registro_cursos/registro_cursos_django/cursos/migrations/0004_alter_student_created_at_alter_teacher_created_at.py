# Generated by Django 5.0.6 on 2024-05-09 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_alter_enrollment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
    ]
