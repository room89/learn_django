import json

import requests

import clients.weather.models as models

def get_weather(city):
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather',
        params={
            'q': city,
            'appid': '2d99318b89600e0b44c3e604229a781d',
        }
    )

    data = json.loads(response.text)

    print(data)

    return models.Weather(data['main']['temp'])