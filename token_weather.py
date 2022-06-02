import requests
from pprint import pprint


def get_weather_request(
    city,
    api_key,
):
    try:
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        )
        # в data хранится список в формате json
        data = response.json()
        # pprint(data)

        # Обращаюсь к словарю в data ы котором хранится json список погоды в городе, температуры и т.д
        name_city = data["name"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        temp = data["main"]["temp"]

        print(f'Ваш город: {name_city}\n'
              f'Влажность в городе {humidity}\nДавление в городе {pressure}\n'
              f'Температура в городе {temp}')

    except Exception as ex:
        print(ex)
        print('Такого города не существует!')


# Запуск кода
if __name__ == '__main__':
    city = input('Назовите город: ')
    get_weather_request(city, api_key='d37a79b496bba43ff51ed9c070d17eb1')
