# Generated by Django 5.0.7 on 2024-07-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Argus_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='current_value',
            field=models.FloatField(blank=True, verbose_name='Единицы измерения'),
        ),
    ]