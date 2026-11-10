dict1 = {"titulo": "Dune", "anio": 2021}
dict2 = {"puntaje": 8, "anio": 2024}

# Caso A: dict1 | dict2 (gana dict2)
resultado_a = dict1 | dict2
print("dict1 | dict2 ->", resultado_a)  

# Caso B: dict2 | dict1 (gana dict1)
resultado_b = dict2 | dict1
print("dict2 | dict1 ->", resultado_b)  