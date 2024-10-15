import random
from pathlib import Path
from Argus_Celery.celery import app
from Argus_Celery.utils import update_sensor_values_from_file
from Argus_App.models import Sensor, MnemonicScheme, HistoricalValue, SMBServers

from smb.SMBConnection import SMBConnection
from io import BytesIO, TextIOWrapper


@app.task
def parse_sensor_values_every_15_seconds():
    """
    Парсинг файлов с точек сбора данных каждые 15 секунд
    """
    smb_servers = SMBServers.objects.all()
    sensors_to_update = []
    historical_values_to_create = []

    for smb_server in smb_servers:
        server_name = smb_server.server_name                    # Полный smb-путь
        server_ip = smb_server.server_ip                        # IP-адрес SMB-сервера
        shared_folder_name = smb_server.shared_folder_name      # Название расшаренной папки
        file_name = smb_server.file_name                        # Путь к файлу внутри расшаренной папки
        user_name = ''                                          # Имя пользователя (для анонимного доступа оставить любым)
        password = ''                                           # Пароль (для анонимного доступа оставить любым)
        client_name = ''                                        # Имя клиента (можно оставить как 'client', для анонимного
                                                                # доступа оставить любым)
        if server_name == 'LAPTOP-PCS7':
            with SMBConnection(user_name, password, client_name, server_name, use_ntlm_v2=True) as conn:
                file_obj = BytesIO()
                try:
                    conn.connect(server_ip)
                    conn.retrieveFile(shared_folder_name, file_name, file_obj)
                    file_obj.seek(0)

                    for i in TextIOWrapper(file_obj, encoding='utf-8'):
                        key, value = i.split('=')
                        value = round(float(value.strip()), 2)

                        sensor = Sensor.objects.get(code=key)
                        sensor.current_value = value
                        sensors_to_update.append(sensor)

                        historical_values_to_create.append(
                            HistoricalValue(value=sensor.current_value,
                                            sensor=sensor)
                        )
                except:
                    pass
        else:
            pass

    Sensor.objects.bulk_update(sensors_to_update, ['current_value'])
    HistoricalValue.objects.bulk_create(historical_values_to_create)

# @app.task
# def fill_historical_values_every_minute():
#     """
#
#     """
#     historical_values_to_create = []
#     for sensor in Sensor.objects.all():
#         historical_values_to_create.append(
#             HistoricalValue(value=sensor.current_value,
#                             sensor=sensor)
#         )
#     HistoricalValue.objects.bulk_create(historical_values_to_create)
