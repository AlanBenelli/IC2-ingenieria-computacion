peliculas = [
    {"titulo": "Dune", "anio": 2021, "director": "denis Villeneuve"},
    {
        "titulo": "battleship: Batalla naval",
        "anio": 2012,
        "director": "Peter Berg",
    },
    {"titulo": "Star Wars: Episodio III – La venganza de los Sith",
      "anio": 2005,
      "director": "George Lucas",
    }
]

director_a_buscar = "Lucas"
encontradas = 0

print(f"Buscando películas del director que contenga: '{director_a_buscar}'")
for p in peliculas:
    if director_a_buscar.lower() in p["director"].lower():
        print(f"  -> Encontrada: {p['titulo']} ({p['anio']})")
        encontradas += 1

if encontradas == 0:
  print("  -> No se encontró ninguna película con ese director.")