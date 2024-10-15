from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def update_sensor_values_from_file(sensor_data_line, sensors, sensors_to_update):
    sensor_data_line = sensor_data_line.strip()
    if sensor_data_line and '=' in sensor_data_line:
        key, val = sensor_data_line.split('=', 1)
        try:
            sensor = sensors.get(code=key)
            value = round(float(val), 2)
            sensor.current_value = value

            sensors_to_update.append(sensor)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            print(key)