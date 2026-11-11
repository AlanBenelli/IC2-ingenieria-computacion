def promedio(notas):
  if not notas:
    return 0
  return sum(notas) / len(notas)

def aprobo(notas):
  return promedio(notas) >= 6

def estadisticas(notas):
  if not notas:
    return {"promedio": 0, "maximo": None, "minimo": None}

  return {
      "promedio": sum(notas) / len(notas),
      "maximo": max(notas),
      "minimo": min(notas),
  }

pelicula = {"titulo": "Transformers: El ùltimo caballero", "anio": 2017, "director": "Michael Bay"}

duracion = pelicula.get("duracion", "desconocido")