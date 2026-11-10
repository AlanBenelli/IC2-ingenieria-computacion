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

print("Títulos en cartelera:")
for p in peliculas:
    print(f"- {p['titulo']}")