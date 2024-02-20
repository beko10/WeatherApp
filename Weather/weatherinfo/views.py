from django.shortcuts import render, redirect
from weatherinfo.forms import WeatherForm
import requests

def get_weather(city):
    api_key = "a15d2e702176a00ae7d1ada18311efc4"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature_celsius = data['main']['temp'] - 273.15 
        return {"city": data['name'], "temperature_celsius": temperature_celsius}
    return None
    

def index(request):
    form = WeatherForm(request.POST or None)
    if form.is_valid():
        city = form.cleaned_data.get("sehir")
        weather_data = get_weather(city)
        if weather_data:
            return render(request, "index.html", {"weather_data": weather_data})
        else:
            return render(request, "index.html", {"form": form, "error_message": "Hava durumu bilgisi alınamadı."})
    
    return render(request, "index.html", {"form": form})





