import requests

api_key = '270b3f38eb48664b4274271dcf256eb6'
country = 'India'

api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={country}"

def fetch_data():
    print(f"trying to fetch data using weather stack api....")
    try:
        response = requests.get(api_url)
        print(f"data fetched succesfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occured : {e}")
        raise


#fetch_data()

def mock_data():
    return {'request': {'type': 'City', 'query': 'Ottawa, Canada', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Ottawa', 'country': 'Canada', 'region': 'Ontario', 'lat': '45.417', 'lon': '-75.700', 'timezone_id': 'America/Toronto', 'localtime': '2026-03-26 13:34', 'localtime_epoch': 1774532040, 'utc_offset': '-4.0'}, 'current': {'observation_time': '05:34 PM', 'temperature': 2, 'weather_code': 296, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0017_cloudy_with_light_rain.png'], 'weather_descriptions': ['Light Rain, Mist'], 'astro': {'sunrise': '06:54 AM', 'sunset': '07:24 PM', 'moonrise': '12:03 PM', 'moonset': '03:48 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 52}, 'air_quality': {'co': '267.85', 'no2': '9.35', 'o3': '84', 'so2': '4.55', 'pm2_5': '19.35', 'pm10': '21.55', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 8, 'wind_degree': 259, 'wind_dir': 'W', 'pressure': 1007, 'precip': 0, 'humidity': 80, 'cloudcover': 100, 'feelslike': 0, 'uv_index': 2, 'visibility': 6, 'is_day': 'yes'}}