import csv
from funciones import analizar_peliculas
from pathlib import Path


def cargar_peliculas(nombre_archivo):
  peliculas = []

  with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
      peliculas.append(fila)

  return peliculas


def main():
  print("--- ANALISIS DE PELICULAS ---")

  archivo_csv = Path(__file__).parent / "peliculas.csv"

  try:
    peliculas = cargar_peliculas(archivo_csv)
  except FileNotFoundError:
    print(f"No se encontro el archivo {archivo_csv}.")
    return

  peliculas_ordenadas = sorted(peliculas, key=lambda pelicula: pelicula["titulo"])

  print("\nListado de peliculas:")
  for pelicula in peliculas_ordenadas:
    print(f"- {pelicula['titulo']} ({pelicula['anio']})")

  resultado = analizar_peliculas(peliculas)

  print("\nEstadisticas:")
  print(f"Cantidad de peliculas: {resultado['cantidad']}")
  print(f"Puntaje promedio: {resultado['promedio']:.2f}")

  if resultado["mejor"] is not None:
    print(
        f"Mejor valorada: {resultado['mejor']['titulo']} "
        f"({resultado['mejor']['puntaje']})"
    )
    print(
        f"Peor valorada: {resultado['peor']['titulo']} "
        f"({resultado['peor']['puntaje']})"
    )

  print("\n--- FIN DEL PROGRAMA ---")


if __name__ == "__main__":
  main()