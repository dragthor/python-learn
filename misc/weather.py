import requests
import datetime
import sys

API_KEY = ""  # Replace with your OpenWeatherMap API key
HEADER = "\033[95m"
ENDC = "\033[0m"

def get_weather_by_zip(zip_code, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "zip": f"{zip_code},us",
        "appid": api_key,
        "units": "imperial"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    zip_code = "08869"

    if len(sys.argv) > 1:
        zip_code = sys.argv[1] # Your USA zip code

    weather_data = get_weather_by_zip(zip_code, API_KEY)
    if weather_data:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        feels_like = weather_data["main"]["feels_like"]
        pressure = weather_data["main"]["pressure"]
        min_temp = weather_data["main"]["temp_min"]
        max_temp = weather_data["main"]["temp_max"]
        sunrise = datetime.datetime.fromtimestamp(weather_data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(weather_data["sys"]["sunset"])

        print(f"{HEADER}Currently in {city} {zip_code}{ENDC}")
        print(f"Temperature: {temperature}°F")
        print(f"Feels like: {feels_like}°F")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Min temperature: {min_temp}°F")
        print(f"Max temperature: {max_temp}°F")
        print(f"Sunrise: {sunrise.strftime("%H:%M:%S")}")
        print(f"Sunset: {sunset.strftime("%H:%M:%S")}")
    else:
        print("Failed to retrieve weather data")
