def promedio(notas):
  if not notas:
    return 0
  return sum(notas) / len(notas)

curso_a = [8, 9, 10, 7]
curso_b = [5, 6, 4, 6]

def aprobo(notas):
  return promedio(notas) >= 6

print("¿El curso A aprobó?:", aprobo(curso_a))
print("¿El curso B aprobó?:", aprobo(curso_b))