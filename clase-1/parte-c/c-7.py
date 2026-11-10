frase = "aprender python es facily python es util, pero c++ es mejor"
palabras = frase.split()
contador = {}

for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print("Frecuencia de palabras:")
print(contador)