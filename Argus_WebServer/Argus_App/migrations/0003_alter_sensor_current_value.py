# Generated by Django 5.0.7 on 2024-07-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Argus_App', '0002_alter_sensor_current_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='current_value',
            field=models.FloatField(blank=True, default=0.0, verbose_name='Единицы измерения'),
        ),
    ]
