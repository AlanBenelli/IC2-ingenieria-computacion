from funciones import promedio

def test_promedio_valores_normales():
  notas = [7, 4, 9, 10, 6]
  assert promedio(notas) == 7.2

  