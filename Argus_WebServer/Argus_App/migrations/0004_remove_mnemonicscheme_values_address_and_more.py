# Generated by Django 5.0.7 on 2024-10-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Argus_App', '0003_alter_sensor_current_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mnemonicscheme',
            name='values_address',
        ),
        migrations.AddField(
            model_name='mnemonicscheme',
            name='file_name',
            field=models.CharField(default='1', max_length=100, verbose_name='Путь к файлу от расшаренной папки'),
        ),
        migrations.AddField(
            model_name='mnemonicscheme',
            name='ip_address',
            field=models.CharField(default='1', max_length=100, verbose_name='Samba-адрес сервера'),
        ),
        migrations.AddField(
            model_name='mnemonicscheme',
            name='server_name',
            field=models.CharField(default='1', max_length=100, verbose_name='Samba-имя сервера'),
        ),
        migrations.AddField(
            model_name='mnemonicscheme',
            name='shared_folder_name',
            field=models.CharField(default='1', max_length=100, verbose_name='Имя расшаренной папки'),
        ),
        migrations.AlterField(
            model_name='mnemonicscheme',
            name='navmenu_name',
            field=models.CharField(default='1', max_length=100, verbose_name='Название для меню'),
        ),
    ]
