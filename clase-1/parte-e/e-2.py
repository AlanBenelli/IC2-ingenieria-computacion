import csv

suma_puntajes = 0.0

with open("peliculas.csv", mode="r", encoding="utf-8") as archivo:
  lector = csv.DictReader(archivo)
  for fila in lector:
    suma_puntajes += float(fila["puntaje"])

print(f"Suma total de puntajes: {suma_puntajes}")