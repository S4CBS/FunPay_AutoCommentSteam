import configparser
from configparser import NoSectionError
def get_cfg():
    try:
        # создаём объекта парсера
        config = configparser.ConfigParser()

        # Чтение файла конфигурации
        config.read('settings.ini')

        # Получение данных из файла конфигурации
        token = config.get(section="FunPay", option="golden_key")
        timer = int(config.get(section="Time", option="time"))

    except NoSectionError as e:

        golden_key = str(input("Введите ваш golden_key: "))
        timer = int(input("Введите время повторяющегося запроса (в секундах): "))

        # Создание кфг
        config = configparser.ConfigParser()

        config.add_section("FunPay")
        config.set(section="FunPay", option="golden_key", value=f"{golden_key}")

        config.add_section('Time')
        config.set(section='Time', option="time", value=f"{timer}")

        # Сохранение конфигурации в файл
        with open('settings.ini', 'w') as config_file:
            config.write(config_file)

        # Чтение файла конфигурации
        config.read('settings.ini')

        # Получение данных из файла конфигурации
        token = config.get(section="FunPay", option="golden_key")
        timer = int(config.get(section="Time", option="time"))

    return token, timer