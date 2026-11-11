def test_pelicula_clave_inexistente():
  pelicula = {"titulo": "Transformers: El ùltimo caballero", "anio": 2017}
  duracion = pelicula.get("duracion", "desconocido")
  assert duracion == "desconocido"