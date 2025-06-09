import requests
from datetime import datetime


def get_current_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\n--- Current Weather ---")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print(f"\nCurrent weather error: {response.status_code}")
        print(response.json())

def get_forecast(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\n--- 5-Day Forecast (3:00 PM) ---")
        for entry in data['list']:
            if "15:00:00" in entry['dt_txt']:
                date = entry['dt_txt'].split(" ")[0]
                temp = entry['main']['temp']
                desc = entry['weather'][0]['description'].capitalize()
                print(f"{date}: {temp}°C, {desc}")
    else:
        print(f"\nForecast error: {response.status_code}")
        print(response.json())

def main():
    city = input("Enter city name: ")
    api_key = "fef33693713b4e969a70056d109b29d8"  
    get_current_weather(city, api_key)
    get_forecast(city, api_key)

if __name__ == "__main__":
    main()