import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Argus_Core.settings')
app = Celery('Argus_Celery',
             broker_connection_retry=False,
             broker_connection_retry_on_startup=True,)

app.config_from_object('django.conf:settings')
broker_connection_retry = False

app.autodiscover_tasks()
app.conf.beat_schedule = {
    # 'send-report-every-single-minute': {
    #     'task': 'Argus_Celery.tasks.parse_sensor_values_every_15_seconds',
    #     'schedule': crontab(),
    # },
    'send-report-every-15-seconds': {
        'task': 'Argus_Celery.tasks.parse_sensor_values_every_15_seconds',
        'schedule': timedelta(seconds=15),
    }
}
