from django.http import HttpResponse

import clients.weather.weatherstack as weather


def index(request):
    weather_data = weather.get_weather('Moscow')
    return HttpResponse(f'{weather_data.temperature - 273.15} C')
