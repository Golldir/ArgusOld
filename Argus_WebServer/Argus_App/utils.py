from pathlib import Path


def parse_sensor_values(file_path):
    '''Парсинг файлов из файла мгновенных значений'''
    values = {}
    file_path = Path(file_path)

    if file_path.exists() and file_path.is_file():
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and '=' in line:
                    key, value = line.split('=', 1)
                    values[key.strip()] = value.strip()

    return values
