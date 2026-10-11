import requests

city_name = input("Enter city name: ")

def get_location(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city
    }

    try:
        response = requests.get(url, params=params)

    except requests.exceptions.RequestException as request_error:
        print(request_error)
        exit()

    if response.status_code != 200:
        print("API request failed")
        exit()

    data = response.json()

    if "results" not in data:
        print("City not found. Please enter a valid city name.")
        raise SystemExit(1)

    results = data["results"]

    location = results[0]

    found_latitude = location["latitude"]
    found_longitude = location["longitude"]
    return found_latitude, found_longitude
latitude, longitude = get_location(city_name)

weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {"latitude": latitude,
                  "longitude": longitude,
                  "current":"temperature_2m,weather_code",
                  "timezone":"auto"}

try:
    weather_response = requests.get(
        weather_url,
        params=weather_params,
        timeout=10
    )

except requests.exceptions.RequestException as e:
    print("Error type:", type(e).__name__)
    print("Error details:", repr(e))
    raise SystemExit(1)

if weather_response.status_code != 200:
    print("API request failed")
    exit()

weather_data = weather_response.json()

current = weather_data["current"]

temperature = current["temperature_2m"]

weather_code = current["weather_code"]

current_time = current["time"]

formatted_time = current_time.replace("T", " "  )

def get_weather_description(code):

    if code == 0:
        return"Clear sky"

    elif code == 1:
        return"Mainly clear"

    elif code == 2:
        return"Partly cloudy"

    elif code == 3:
        return"Overcast"

    elif code in (61, 63, 65):
        return"Rain"

    elif code in (71, 73, 75, 77):
        return"Snow"

    elif code in (80, 81, 82):
        return"Rain showers"

    elif code == 95:
        return"Thunderstorm"

    return"Unknown weather"

description = get_weather_description(weather_code)

print("City       : ", city_name)
print("Time       : ", formatted_time)
print("Temperature: ",temperature )
print("Condition  :",description)








