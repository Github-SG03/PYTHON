#Main Program: weather_app.py

import requests

def get_weather(city_name, api_key):
    """
    Fetch weather data for a given city using the OpenWeatherMap API.

    Args:
        city_name (str): The name of the city.
        api_key (str): API key for OpenWeatherMap.

    Returns:
        dict: Weather information if successful, or an error message.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx

        data = response.json()
        weather_info = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Humidity": f"{data['main']['humidity']}%",
        }
        return weather_info

    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

    except KeyError:
        return {"Error": "Unable to parse weather data. Please check the city name."}


if __name__ == "__main__":
    print("Weather Information Application")
    api_key = input("Enter your OpenWeatherMap API key: ")  # Get API key from the user

    while True:
        city = input("\nEnter a city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Exiting the application. Goodbye!")
            break

        weather = get_weather(city, api_key)
        if "Error" in weather:
            print(f"Error: {weather['Error']}")
        else:
            print("\nWeather Information:")
            for key, value in weather.items():
                print(f"{key}: {value}")