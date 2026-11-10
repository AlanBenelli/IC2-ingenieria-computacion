alumnos = range(1, 31)

pares = [n for n in alumnos if n % 2 == 0]
impares = [n for n in alumnos if n % 2 != 0]

print(f"Cantidad en grupo par: {len(pares)}")
print(f"Cantidad en grupo impar: {len(impares)}")
print(f"Suma total de los grupos: {len(pares) + len(impares)}")