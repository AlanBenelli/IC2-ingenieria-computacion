import csv

print("--- Contenido de peliculas.csv ---")
with open("peliculas.csv", mode="r", encoding="utf-8") as archivo:
  lector = csv.DictReader(archivo)
  for fila in lector:
    print(fila)