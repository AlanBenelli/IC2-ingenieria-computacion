import csv

acumulador_generos = {}

with open("peliculas.csv", mode="r", encoding="utf-8") as archivo:
  lector = csv.DictReader(archivo)
  for fila in lector:
    genero = fila["genero"]
    puntaje = float(fila["puntaje"])

    if genero not in acumulador_generos:
      acumulador_generos[genero] = {"suma": 0.0, "cantidad": 0}

    acumulador_generos[genero]["suma"] += puntaje
    acumulador_generos[genero]["cantidad"] += 1

promedios_por_genero = {}
for genero, datos in acumulador_generos.items():
  promedios_por_genero[genero] = datos["suma"] / datos["cantidad"]

print("Promedio de puntaje por género:")
for genero, prom in promedios_por_genero.items():
  print(f"- {genero}: {prom:.2f}")