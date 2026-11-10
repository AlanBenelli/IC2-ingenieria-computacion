def estadisticas(notas):
  if not notas:
    return {"promedio": 0, "maximo": 0, "minimo": 0}
  return {
      "promedio": sum(notas) / len(notas),
      "maximo": max(notas),
      "minimo": min(notas),
  }

def reporte(notas):
  stats = estadisticas(notas)
  return (
      f"Promedio: {stats['promedio']:.1f} | Máximo: {stats['maximo']} | Mínimo:"
      f" {stats['minimo']}"
  )

notas_alumno = [7, 4, 9, 10, 6]
print(reporte(notas_alumno))