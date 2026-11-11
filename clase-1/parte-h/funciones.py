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

def analizar_peliculas(peliculas):
  if not peliculas:
    return {
        "cantidad": 0,
        "promedio": 0,
        "mejor": None,
        "peor": None,
    }

  puntajes = [float(pelicula["puntaje"]) for pelicula in peliculas]

  mejor = max(peliculas, key=lambda pelicula: float(pelicula["puntaje"]))
  peor = min(peliculas, key=lambda pelicula: float(pelicula["puntaje"]))

  return {
      "cantidad": len(peliculas),
      "promedio": sum(puntajes) / len(puntajes),
      "mejor": mejor,
      "peor": peor,
  }