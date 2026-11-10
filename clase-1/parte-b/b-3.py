puntajes = [120, 45, 300, 80, 210]

max_for = puntajes[0]
min_for = puntajes[0]
suma_total = 0

for p in puntajes:
  if p > max_for:
    max_for = p
  if p < min_for:
    min_for = p
  suma_total += p

promedio_for = suma_total / len(puntajes)
print(f"Máximo: {max_for} | Mínimo: {min_for} | Promedio: {promedio_for}")


print(
    f"Máximo: {max(puntajes)} | Mínimo: {min(puntajes)} | Promedio:"
    f" {sum(puntajes) / len(puntajes)}"
)