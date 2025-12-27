import os
from dotenv import load_dotenv
import requests

load_dotenv()

city = input("Enter city name: ").strip()

api_key = os.getenv("WEATHER_API_KEY")

if not api_key:
    print("API key not found! Please add it to the .env file.")
    exit()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    condition = data['weather'][0]['description']
    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {condition}")
else:
    data = response.json()
    print(f"Error {response.status_code}: {data.get('message', 'Unknown error')}")
