import os
import requests
from pprint import pprint
from datetime import datetime
from dotenv import load_dotenv
import locale

# функция отвечабщая за язык печати
# locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


def get_weather_request(city, api_key):
    try:

        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        )

        # в data хранится список в формате json
        data = response.json()
        # pprint(data)

        # Обращаюсь к словарю в data ы котором хранится json список погоды в городе, температуры и т.д
        name_city = data["name"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]

        return f'{datetime.now().strftime("%d %B %Y")}\nВаш город: {name_city}\nВлажность в городе {humidity}\nДавление в городе {pressure}\nТемпература в городе {temp}\nСкорость ветра {wind}'

    # исключение на не существующий город
    except Exception as ex:
        print(ex)
        return 'Такого города не существует!'


if __name__ == '__main__':
    # инпут работает по default='ru-en'
    load_dotenv()
    city = input('Назовите город: ')
    get_weather_request(city, api_key=os.environ.get('WEATHER_GET_APITOKEN'))
