import unittest
import funct

def testing_same_city(city1, country1, lat1, lon1, city2, country2, lat2, lon2):
    ## Misma ciudad
    ## Requiere haber corrido el programa anterior
    assert funct.get_city_coordinates(city1,country1)==lat1,lon1
    assert funct.get_city_coordinates(city2,country2)==lat1,lon1
    assert funct.haversine(lat1,lon1,lat2,lon2)==0
