import unittest
import funct

class TestCityFunctions(unittest.TestCase):
    def Success_case(city1,city2,country1,country2,switch):
        if switch==1:
            lat1, lon1 = funct.get_city_coordinates(city1,country1)
            lat2, lon2 = funct.get_city_coordinates(city2,country2)
        elif switch==2:
            lat1, lon1 = funct.get_coordinates(city1,country1)
            lat2, lon2 = funct.get_coordinates(city2,country2)
        distance = funct.haversine(lat1, lon1, lat2, lon2)
        print("Son ciudades y países diferentes, entonces esta es la distancia  {distance} ")

    def test_unknown_city_csv(self):
        city1, country1 = "UnknownCity1", "Country1"
        city2, country2 = "UnknownCity2", "Country2"
        lat1, lon1 = funct.get_city_coordinates(city1, country1)
        lat2, lon2 = funct.get_city_coordinates(city2, country2)
        self.assertIsNone(lat1, f"La ciudad '{city1}' no se encontró en el archivo.")
        self.assertIsNone(lon1, f"La ciudad '{city1}' no se encontró en el archivo.")
        self.assertIsNone(lat2, f"La ciudad '{city2}' no se encontró en el archivo.")
        self.assertIsNone(lon2, f"La ciudad '{city2}' no se encontró en el archivo.")

    def test_unknown_city_api(self):
        city1, country1 = "UnknownCity1", "Country1"
        city2, country2 = "UnknownCity2", "Country2"
        lat1, lon1 = funct.get_coordinates(city1, country1)
        lat2, lon2 = funct.get_coordinates(city2, country2)
        self.assertIsNone(lat1, f"No se encontraron coordenadas para {city1}, {country1}.")
        self.assertIsNone(lon1, f"No se encontraron coordenadas para {city1}, {country1}.")
        self.assertIsNone(lat2, f"No se encontraron coordenadas para {city2}, {country2}.")
        self.assertIsNone(lon2, f"No se encontraron coordenadas para {city2}, {country2}.")

    def test_same_city_csv(self):
        city, country = "Lima", "Peru"
        lat1, lon1 = funct.get_city_coordinates(city, country)
        lat2, lon2 = funct.get_city_coordinates(city, country)
        distance = funct.haversine(lat1, lon1, lat2, lon2)
        self.assertEqual(distance, 0, "La distancia debe ser cero para la misma ciudad y país usando CSV.")

    def test_same_city_api(self):
        city, country = "Lima", "Peru"
        lat1, lon1 = funct.get_coordinates(city, country)
        lat2, lon2 = funct.get_coordinates(city, country)
        distance = funct.haversine(lat1, lon1, lat2, lon2)
        self.assertEqual(distance, 0, "La distancia debe ser cero para la misma ciudad y país usando la API.")

if __name__ == "__main__":
    unittest.main()
