import csv

total_peliculas = 0
suma_puntajes = 0.0
mejor_pelicula = None
max_puntaje = -1.0

with open("peliculas.csv", mode="r", encoding="utf-8") as archivo:
  lector = csv.DictReader(archivo)
  for fila in lector:
    total_peliculas += 1
    puntaje = float(fila["puntaje"])
    suma_puntajes += puntaje

    if puntaje > max_puntaje:
      max_puntaje = puntaje
      mejor_pelicula = fila["titulo"]

if total_peliculas > 0:
    promedio_puntajes = suma_puntajes / total_peliculas
else:
    promedio_puntajes = 0

print(f"Cantidad de películas: {total_peliculas}")
print(f"Puntaje promedio: {promedio_puntajes:.2f}")
print(f"Mejor película: {mejor_pelicula} (con {max_puntaje} puntos)")