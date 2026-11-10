def promedio(notas):
  if not notas:
    return 0
  return sum(notas) / len(notas)

curso_a = [8, 9, 10, 7]
curso_b = [5, 6, 4, 6]

print(f"Promedio Curso A: {promedio(curso_a)}")
print(f"Promedio Curso B: {promedio(curso_b)}")