import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=24.71&longitude=46.67&current=temperature_2m"

response = requests.get(url)

data = response.json()

print("Temperature:", data["current"]["temperature_2m"], "°C")