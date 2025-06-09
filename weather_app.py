import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())


def main():
    city = input("Enter city name: ")
    api_key = "Enter your api key here"
    get_weather(city, api_key)

if __name__ == "__main__":
    main()