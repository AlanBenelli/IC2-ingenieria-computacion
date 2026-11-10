lecturas = [10, 20, 15, 25, 30, 22, 18, 35, 40, 38]
ventana = 3
promedios_lecturas = []

for i in range(len(lecturas) - ventana + 1):
  sub_lista = lecturas[i : i + ventana]
  promedio = sum(sub_lista) / ventana
  promedios_lecturas.append(promedio)

print(f"Lecturas originales ({len(lecturas)} elementos): {lecturas}")
print(f"Promedios móviles ({len(promedios_lecturas)} elementos): {promedios_lecturas}")