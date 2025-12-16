#Console-based Weather Application using Python and OpenWeather API

import requests

def weather_app():
    print("=== Weather App Using API ===")

    city = input("Enter city name: ").strip()

    if city == "":
        print("City name cannot be empty!")
        return

    api_key = "b291c343b0b2bb12d7d13d6cdb5c9af6"  

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_condition = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            print("\n--- Weather Details ---")
            print(f"City: {city_name}")
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity} %")
            print(f"Weather Condition: {weather_condition.capitalize()}")
            print(f"Wind Speed: {wind_speed} m/s")

        else:
            print("\nError: City not found or invalid API key.")

    except Exception as e:
        print("Something went wrong:", e)


# Run the app
weather_app()

