import pandas as pd
import requests
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    return distance

def get_city_coordinates(city_name, country):
    cities = pd.read_csv("worldcities.csv")
    city = cities[
        (cities['city'].str.lower() == city_name.lower()) &
        (cities['country'].str.lower() == country.lower())
    ]
    if city.empty:
        print(f"La ciudad '{city_name}' no se encontró en el archivo.")
        return None, None
    a=float(city.iloc[0]['lat'])
    b= float(city.iloc[0]['lng'])
    print(f"La latitud y longitud de {city_name}:{country} es {a} y {b}")

    return float(city.iloc[0]['lat']), float(city.iloc[0]['lng'])  #Sacar un longitud y latitud


def get_coordinates(city, country):
    """Consulta la API de Nominatim y valida los resultados."""
    url = f"https://nominatim.openstreetmap.org/search?q={city},{country}&format=json"

    # Agregar un encabezado User-Agent
    headers = {
        "User-Agent": "MiAplicacion/1.0 (lando.veramendi@utec.edu.pe)"  # Cambia esto por tu propia información
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200 and response.json():
        data = response.json()  # Obtener todos los resultados

        # Tomar el primer resultado
        first_result = data[0]
        lat, lon = float(first_result['lat']), float(first_result['lon'])

        # Mostrar información adicional
        print(f"Coordenadas encontradas: {lat}, {lon} para {city}, {country}")

        return lat, lon
    else:
        print(f"No se encontraron coordenadas para {city}, {country}. Código de estado: {response.status_code}")
        return None, None

def mock():
    """Mock: Devuelve coordenadas fijas para pruebas."""
    print("Usando mock: Devuelve siempre las coordenadas de Lima y Buenos Aires.")
    lat1, lon1 = -12.0464, -77.0428  # Lima, Perú
    lat2, lon2 = -34.6037, -58.3816  # Buenos Aires, Argentina
    print(haversine(lat1, lon1, lat2, lon2),"km")
