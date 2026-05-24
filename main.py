import requests

# Riyadh coordinates
latitude = 24.71
longitude = 46.67

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,wind_speed_10m"
)

response = requests.get(url)

data = response.json()

temperature = data["current"]["temperature_2m"]
wind_speed = data["current"]["wind_speed_10m"]

print("\n=== Current Weather in Riyadh ===")
print(f"Temperature : {temperature} °C")
print(f"Wind Speed  : {wind_speed} km/h")