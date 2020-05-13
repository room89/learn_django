import requests

import clients.weather.models as models

def get_weather(city):
    # https://weatherstack.com/documentation
    access_key = 'DuW5hFu1vJpqjdUSToDHFvWJDvCIFMvA'
    response = requests.get(
        'http://api.weatherstack.com/current',
        params={
        }
    )

    return models.Weather(temperature=273.15)
