import requests
import datetime
import sys

# Usage: python3 weather.py <api_key> <zip_code>

class colors:
    HEADER = "\033[95m"
    ENDC = "\033[0m"
    FAIL = "\033[91m"

def get_weather_by_zip(zip_code: int, api_key : str):
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
    zip_code = "08869" # Default to the coolest town in NJ.
    api_key = ""

    if len(sys.argv) > 2:
        api_key = sys.argv[1] # Your OpenWeatherMap API key
        zip_code = sys.argv[2] # Your USA zip code

    if len(zip_code) != 5:
        print("Error: Zip code must be 5 characters long.")
        sys.exit(1)
        
    if not zip_code.isdigit():
        print("Error: Zip code must be numeric.")
        sys.exit(1)

    if (len(api_key) <= 0):
        print("Error: API key is required.")
        sys.exit(1)

    weather_data = get_weather_by_zip(zip_code, api_key)
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

        print(f"{colors.HEADER}Currently in {city} {zip_code}{colors.ENDC}")
        print(f"Temperature: {temperature}°F")
        print(f"Feels like: {feels_like}°F")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Min temperature: {min_temp}°F")
        print(f"Max temperature: {max_temp}°F")
        print(f"Sunrise: {sunrise.strftime("%H:%M:%S")}")
        print(f"Sunset: {sunset.strftime("%H:%M:%S")}")
    else:
        print(f"{colors.FAIL}Failed to retrieve weather data.{colors.ENDC}")
