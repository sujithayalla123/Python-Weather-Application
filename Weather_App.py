import requests
print("======WEATHER APPLICATION======")
city=input("Enter the city name:")
print("Getting weather information for", city)
print("Requests library is ready!")
url = "https://geocoding-api.open-meteo.com/v1/search"
try:
    response = requests.get(url, params={
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
    },timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException:
    print("Unable to connect. Please check your internet connection.")
    exit()
if "results" not in data:
    print("City not found! Please enter a valid city name.")

else:
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"
    try:
        weather_response = requests.get(weather_url, params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        })
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        current = weather_data["current"]
        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        print("\n===== CURRENT WEATHER =====")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "km/h")
    except requests.exceptions.RequestException:
            print("Unable to get weather. Please check your internet connection.")