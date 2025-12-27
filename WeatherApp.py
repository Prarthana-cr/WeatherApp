import requests

city = input("Enter city name: ").strip()

api_key = "4dc73d599288a4506394bf4927de7022"

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
