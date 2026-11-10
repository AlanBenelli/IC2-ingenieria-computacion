import csv

genero_buscado = "Sci-Fi"
archivo_entrada = "peliculas.csv"
archivo_salida = "filtradas.csv"

peliculas_filtradas = []

with open(archivo_entrada, mode="r", encoding="utf-8") as entrada:
  lector = csv.DictReader(entrada)
  columnas = lector.fieldnames  
  for fila in lector:
    if fila["genero"].strip().lower() == genero_buscado.lower():
      peliculas_filtradas.append(fila)

with open(
    archivo_salida, mode="w", newline="", encoding="utf-8"
) as salida:
  escritor = csv.DictWriter(salida, fieldnames=columnas)
  escritor.writeheader()
  escritor.writerows(peliculas_filtradas)

print(
    f"Archivo '{archivo_salida}' creado con éxito con"
    f" {len(peliculas_filtradas)} películas de '{genero_buscado}'."
)