def promedio(notas):
  if not notas:
    return 0
  return sum(notas) / len(notas)

curso_a = [8, 9, 10, 7]
curso_b = [5, 6, 4, 6]

def aprobo(notas, minimo=6):
  return promedio(notas) >= minimo

print("Aprobado con mínimo por defecto (6):", aprobo([5.5, 6, 6.5]))

print("Aprobado exigiendo mínimo de 7:", aprobo([5.5, 6, 6.5], minimo=7))