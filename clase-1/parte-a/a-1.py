notas = [7, 4, 9, 10, 6]

promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio}")

if promedio >= 6:
  print("Estado: Aprobó")
else:
  print("Estado: Desaprobó")