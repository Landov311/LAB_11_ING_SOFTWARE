# LAB_11_ING_SOFTWARE
Pruebas de éxito y 2 casos extremos

**Links de tablas:**
Casos de Prueba

Casos Extremos
https://drive.google.com/file/d/1hJ5jRQSHDH3mAptd3FDgBcKa5xtsUZ9L/view?usp=sharing


***CASOS EXTREMOS***

**Caso Extremo:** ciudad desconocida

**Precondicion:** Por lo menos una de las ciudades no es accesible en la API o no existe en el dataset "worldcities.csv"

**Pasos de Prueba:**
1. Correr el codigo.
2. escoger la fuente a usar (opciones 1, 2 o 3).
3. Ingresar el nombre de una ciudad que no existe. Luego, ingresar la segunda ciudad (imaginaria o no).
4. Ingresar los paises de las dos ciudades correspondientes.
5. Presionar la tecla "Enter".

**Text Data:**
- city1, country1 = "UnknownCity1", "Country1"
- city2, country2 = "UnknownCity2", "Country2"

**Resultado Esperado:** Mostrara los siguientes mensajes "No se pudo calcular la distancia. Verifique los nombres de las ciudades.

**Caso Extremo:** misma ciudad

**Precondicion:** Se ingresa la misma ciudad en ambos imputs de ciudad y el mismo pais.

**Pasos de Prueba:**
1. Correr el código.
2. Escoger la fuente a usar (cualquiera)
3. Ingresar el nombre de una ciudad dos veces.
4. Ingresar el nombre del país que corresponde a la ciudad 2 veces.
5. Presionar la tecla "Enter".

**Text Data:**
- city1: Tokyo o Tokio
- city2: Tokyo o Tokio
- country1: Japan o Japon
- country2: Japan o Japon

**Resultado Esperado:** Se muestran las coordenadas de la ciudad 2 veces y la distancia es igual a 0.