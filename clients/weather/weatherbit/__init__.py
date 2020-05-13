import requests

import clients.weather.models as models

def get_weather(city):
    # https://www.weatherbit.io/api/weather-current
    api_key = 'dc0c2cf4677442d3b043e48a95e0c799'
    response = requests.get(
        'http://api.weatherstack.com/current',
        params={
        }
    )

    return models.Weather(temperature=273.15)
