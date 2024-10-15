import datetime
from pathlib import Path
from django.shortcuts import render, get_object_or_404
from django_user_agents.utils import get_user_agent
from .models import MnemonicScheme


def fill_template_from_db(request, slug):
    """
    Запрашивает из БД:
        1. Все схемы, нужны конкретно названия схем для меню
        2. Схему, соответствующую слагу
        3. Все датчики выбранной схемы

    Из запроса пользователя берем название браузера, чтобы выдать новую или старую тему
    """
    schemes = MnemonicScheme.objects.all()  # Все строки со схемами
    scheme = get_object_or_404(schemes, slug=slug) # Схема, которую вызвал пользователь

    sensors = scheme.sensors.all()  # Все датчики выбранной схемы

    browser_name = get_user_agent(request)
    version_check = ('old', True) if 'IE' in str(browser_name) else ('new', False)

    return render(request, f'{version_check[0]}/base.html', {
        'schemes': schemes, 'scheme': scheme, 'sensors': sensors,
        'time': datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        'ie_check': version_check[1],
    })

