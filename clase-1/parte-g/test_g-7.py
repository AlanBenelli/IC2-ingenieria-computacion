import pytest
from funciones import aprobo

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