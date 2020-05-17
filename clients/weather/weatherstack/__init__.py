import requests

import clients.weather.models as models

def get_weather(city):
    # https://weatherstack.com/documentation
    access_key = '4a525fe4deab4bf629b47641eb9afa01'
    response = requests.get(
        'http://api.weatherstack.com/current',
        params={
            'access_key': access_key,
            'query': city,
            'units': 's',
        }
    )
    temperature = response.json()['current']['temperature']
    print (response.json())
    print (type(response.text))
    return models.Weather(temperature=temperature)
