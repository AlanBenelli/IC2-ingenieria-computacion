puntajes = [120, 45, 300, 80, 210]

# 1 Usando sorted()
ranking_copia = sorted(puntajes, reverse=True)
print("Ranking con sorted():", ranking_copia)
print("Original intacta tras sorted():", puntajes)

# 2 Usando .sort() 
puntajes.sort(reverse=True)
print("Ranking con .sort():", puntajes)