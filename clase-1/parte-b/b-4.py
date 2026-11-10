puntajes = [120, 45, 300, 80, 210]
puntajes_filtrados = [p for p in puntajes if p > 100]

print("Lista original intacta:", puntajes)
print("Nueva lista filtrada mayores a 100:", puntajes_filtrados)