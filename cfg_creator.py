import configparser
from configparser import NoSectionError
import os


def get_cfg():
    try:
        # создаём объекта парсера
        config = configparser.ConfigParser()

        # Чтение файла конфигурации
        config.read('settings.ini')

        # Получение данных из файла конфигурации
        token = config.get(section="FunPay", option="golden_key")
        timer = int(config.get(section="Time", option="time"))
        user_agent = config.get(section="Web", option="UserAgent")

    except NoSectionError as e:

        golden_key = str(input("Введите ваш golden_key: "))
        timer = int(input("Введите время повторяющегося запроса (в секундах): "))
        user_agent = str(input("Введите ваш UserAgent (https://whatmyuseragent.com/): "))

        os.system("cls")

        # Создание кфг
        config = configparser.ConfigParser()

        config.add_section("FunPay")
        config.set(section="FunPay", option="golden_key", value=f"{golden_key}")

        config.add_section('Time')
        config.set(section='Time', option="time", value=f"{timer}")

        config.add_section("Web")
        config.set(section="Web", option="UserAgent", value=f"{user_agent}")

        # Сохранение конфигурации в файл
        with open('settings.ini', 'w') as config_file:
            config.write(config_file)

        # Чтение файла конфигурации
        config.read('settings.ini')

        # Получение данных из файла конфигурации
        token = config.get(section="FunPay", option="golden_key")
        timer = int(config.get(section="Time", option="time"))
        user_agent = config.get(section="Web", option="UserAgent")

    return token, timer, user_agent
