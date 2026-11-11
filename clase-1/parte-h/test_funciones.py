import pytest
from funciones import aprobo, estadisticas, promedio

def test_promedio_valores_normales():
  notas = [7, 4, 9, 10, 6]
  assert promedio(notas) == 7.2


def test_aprobo_caso_exitoso():
  assert aprobo([8, 8, 8]) == True

def test_aprobo_caso_reprobado():
  assert aprobo([4, 3, 5]) == False

def test_aprobo_caso_limite():
  assert aprobo([6, 6, 6]) == True


def test_estadisticas_calculo_correcto():
  resultado = estadisticas([7, 4, 9, 10, 6])
  assert resultado["promedio"] == 7.2
  assert resultado["maximo"] == 10
  assert resultado["minimo"] == 4


def test_pelicula_clave_inexistente():
  pelicula = {"titulo": "Transformers: El ùltimo caballero", "anio": 2017}
  duracion = pelicula.get("duracion", "desconocido")
  assert duracion == "desconocido"


def test_promedio_lista_vacia():
  assert promedio([]) == 0


@pytest.mark.parametrize(
    "notas, esperado",
    [
        ([8, 9, 7], True), 
        ([3, 4, 5], False),  
        ([6, 6, 6], True),  
    ],
)

def test_aprobo_varios_casos(notas, esperado):
  assert aprobo(notas) == esperado