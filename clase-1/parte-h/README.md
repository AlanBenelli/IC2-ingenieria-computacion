# Mini-Proyecto Python: Análisis de Películas

## Requisitos
- Python 3
- pytest

## Estructura del proyecto
- `main.py`: carga el archivo CSV y muestra el listado y las estadísticas.
- `funciones.py`: contiene las funciones de cálculo y análisis.
- `peliculas.csv`: contiene los datos de las películas.
- `test_funciones.py`: contiene las pruebas automatizadas.

## Cómo ejecutar el programa

Desde la raíz del repositorio:

```bash
python clase-1/parte-h/main.py
```

## Cómo ejecutar los tests

Desde la raíz del repositorio:

```bash
pytest clase-1/parte-h/ -v
```

## Estadísticas calculadas
El programa muestra:
- Cantidad total de películas.
- Puntaje promedio.
- Película mejor valorada.
- Película peor valorada.

También presenta el listado de películas ordenado alfabéticamente por título.

## Datos
Los datos se obtienen del archivo `peliculas.csv`, que contiene título, año, puntaje y género.