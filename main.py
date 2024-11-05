import funct

def main():
   print("Selccione la forma en el cual desea obtener su respuesta:")
   print("Ingrese 1 para usar csv:")
   print("Ingrese 2 para usar una API:")
   print("Ingrese 3 para usar mock:")
   switch = input("valor: ")
   if switch == "3":
      funct.mock()
      return
   city1 = input("Ingrese el nombre de la primera ciudad: ")
   city2 = input("Ingrese el nombre de la segunda ciudad: ")
   country1 = input("Ingrese el nombre del país de la primera ciudad: ")
   country2 = input("Ingrese el nombre del país de la segunda ciudad: ")


   if switch == "1":
      lat1, lon1 = funct.get_city_coordinates(city1,country1)
      lat2, lon2 = funct.get_city_coordinates(city2,country2)
      if None in (lat1, lon1, lat2, lon2):
        print("No se pudo calcular la distancia. Verifique los nombres de las ciudades.")
        return
      distance = funct.haversine(lat1, lon1, lat2, lon2)
      print(f"La distancia entre {city1} y {city2}, usando CSV es de {distance:.2f} km.")
   elif switch == "2":
      lat1, lon1 = funct.get_coordinates(city1,country1)
      lat2, lon2 = funct.get_coordinates(city2,country2)
      if None in (lat1, lon1, lat2, lon2):
        print("No se pudo calcular la distancia. Verifique los nombres de las ciudades.")
        return
      distance = funct.haversine(lat1, lon1, lat2, lon2)
      print(f"La distancia entre {city1} y {city2}, usando la API es de {distance:.2f} km.")
   else:
      print("valor no valido")
      return


if __name__ == "__main__":
    main()