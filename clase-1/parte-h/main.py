# main.py
import csv
from funciones import obtener_valor  


def cargar_peliculas(nombre_archivo):
  """Lee el archivo CSV y devuelve una lista de diccionarios con las películas."""
  peliculas = []
  with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
      peliculas.append(fila)
  return peliculas


def main():
  print("--- INICIO DEL MINI-PROYECTO ---")

  archivo_csv = "peliculas.csv"
  try:
    peliculas = cargar_peliculas(archivo_csv)
    print(f"Se cargaron {len(peliculas)} películas correctamente.\n")
  except FileNotFoundError:
    print(
        f"No se encontró el archivo {archivo_csv}. Asegurate de tenerlo en la"
        " carpeta."
    )
    return

  print("Listado y procesamiento de datos:")
  for pelicula in peliculas:
    titulo = pelicula.get("titulo", "Sin título")
    anio = pelicula.get("anio", "Desconocido")
    print(f"- {titulo} ({anio})")

  print("\n--- FIN DEL PROGRAMA ---")


if __name__ == "__main__":
  main()