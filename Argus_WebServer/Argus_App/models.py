from django.db import models


class MnemonicScheme(models.Model):
    """
    Модель для хранения мнемосхем.
    """
    image = models.ImageField(upload_to='photos/', blank=False, verbose_name='Мнемосхема')
    slug = models.SlugField(max_length=30, blank=False, unique=True, db_index=True, verbose_name='Слаг')
    navmenu_name = models.CharField(max_length=100, blank=False, default='1', verbose_name='Название для меню')

    class Meta:
        verbose_name = "Мнемосхема"
        verbose_name_plural = "Мнемосхемы"
        ordering = ['navmenu_name']

    def __str__(self):
        return self.navmenu_name


class SMBServers(models.Model):
    server_ip = models.CharField(max_length=100, blank=False, verbose_name='Samba-адрес сервера')
    server_name = models.CharField(max_length=100, blank=False, verbose_name='Samba-имя сервера')
    shared_folder_name = models.CharField(max_length=100, blank=False,verbose_name='Имя расшаренной папки')
    file_name = models.CharField(max_length=100, blank=False, verbose_name='Путь к файлу от расшаренной папки')

    class Meta:
        verbose_name = "Samba-сервер"
        verbose_name_plural = "Samba-сервера"

    def __str__(self):
        return self.server_name

class Sensor(models.Model):
    """
    Модель для хранения датчиков, располагаемых на мнемосхемах.
    """
    code = models.CharField(max_length=100, verbose_name='Номер датчика')
    pos_x = models.CharField(max_length=100, verbose_name='Координата X')
    pos_y = models.CharField(max_length=100, verbose_name='Координата Y')
    center = models.BooleanField(default=False, verbose_name='Центрирование')  # ???????????????????????????????
    color = models.CharField(max_length=100, verbose_name='Цвет')
    units = models.CharField(max_length=100, verbose_name='Единицы измерения')
    current_value = models.FloatField(verbose_name='Единицы измерения', blank=True, default=0.0)
    scheme = models.ForeignKey('MnemonicScheme', on_delete=models.DO_NOTHING, related_name='sensors', null=True)

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"

    def __str__(self):
        return self.code


class HistoricalValue(models.Model):
    """
    Модель для хранения исторических значений датчиков.
    """
    value = models.CharField(max_length=100, verbose_name='Актуальное значение', null=True)
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время обработки')
    sensor = models.ForeignKey('Sensor', on_delete=models.DO_NOTHING, related_name='historic_values', null=True)

    class Meta:
        verbose_name = "Историческое значение"
        verbose_name_plural = "Исторические значения"
        ordering = ['-creation_time']


    def __str__(self):
        return f"{self.sensor.code} - {self.value} в {self.creation_time}"
