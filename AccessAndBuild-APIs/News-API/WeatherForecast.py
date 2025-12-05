import requests

def get_weather(city, api_key='4de352b7f8fc0f5ea3bdc0924662417e'):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    r = requests.get(url)
    content = r.json()
    forecasts = content['list']
    for forecast in forecasts:
        dt_txt = forecast['dt_txt']
        temp_k = forecast['main']['temp']
        temp_c = temp_k - 273.15
        weather_desc = forecast['weather'][0]['description']
        print(f"Date & Time: {dt_txt}, Temperature: {temp_c:.2f}°C, Weather: {weather_desc}")
print(get_weather(city='Badulla'))