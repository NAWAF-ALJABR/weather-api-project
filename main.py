import requests
#اسم المدينه عشان نسحب الطقس الخاص بها من API
city = input("Enter city name: ")

# Geocoding API
geo_url = (
    f"https://geocoding-api.open-meteo.com/v1/search?"
    f"name={city}&count=1&language=en&format=json"
)

geo_response = requests.get(geo_url)
geo_data = geo_response.json()0
#احداثيات المدينه
# Get coordinates
latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]

# Weather API
weather_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,wind_speed_10m"
)

weather_response = requests.get(weather_url)
weather_data = weather_response.json()

temperature = weather_data["current"]["temperature_2m"]
wind_speed = weather_data["current"]["wind_speed_10m"]
#طباعة التفاصيل للحرارة وسرعة الرياح
print(f"\n=== Current Weather in {city.title()} ===")
print(f"Temperature : {temperature} °C")
print(f"Wind Speed  : {wind_speed} km/h")