from funciones import aprobo

def test_aprobo_caso_exitoso():
  assert aprobo([8, 8, 8]) == True

def test_aprobo_caso_reprobado():
  assert aprobo([4, 3, 5]) == False

def test_aprobo_caso_limite():
  assert aprobo([6, 6, 6]) == True
  