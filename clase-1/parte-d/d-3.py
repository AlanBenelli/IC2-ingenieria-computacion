def estadisticas(notas):
  if not notas:
    return {"promedio": 0, "maximo": None, "minimo": None}

  return {
      "promedio": sum(notas) / len(notas),
      "maximo": max(notas),
      "minimo": min(notas),
  }

resultado_stats = estadisticas([7, 4, 9, 10, 6])
print("Diccionario de estadísticas:", resultado_stats)