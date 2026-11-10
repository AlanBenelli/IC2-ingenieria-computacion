pelicula = {"titulo": "Transformers: El ùltimo caballero", "anio": 2017, "director": "Michael Bay"}

print(pelicula["duracion"])

# .get()
duracion = pelicula.get("duracion", "desconocido")
print(f"Duración: {duracion}")
