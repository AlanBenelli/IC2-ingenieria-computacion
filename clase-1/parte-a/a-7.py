km_iniciales = 50  

# Factores de conversión
KM_A_MILLAS = 1.60934
PIES_POR_MILLA = 5280

millas = km_iniciales / KM_A_MILLAS
pies = millas * PIES_POR_MILLA

print(f"Distancia original: {km_iniciales} km")
print(f"En millas: {millas:.2f}")
print(f"En pies: {pies:.2f}")