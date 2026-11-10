def promedio(notas):
  if len(notas) == 0:
    print("Se esta intentando calcular el promedio de una lista vacía.")
    return 0  

  return sum(notas) / len(notas)

print("Promedio de lista vacía:", promedio([]))