# Generated by Django 5.0.4 on 2024-05-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorResultados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='calificacion',
            field=models.IntegerField(verbose_name='Calificaci´pn Final'),
        ),
    ]