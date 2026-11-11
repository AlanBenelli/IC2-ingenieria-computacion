# Ejercicio G8 — Compartir los tests con el equipo

1. **Verificar los archivos:**

   Tener listos los archivos de código (`funciones.py`) y los tests (`test_*.py`) dentro de la carpeta del proyecto.

2. **Agregar los cambios al Stage:**

   Desde la carpeta del proyecto:

   ```bash
   git add test_*.py funciones.py
   ```

3. **Crear un commit:**

   ```bash
   git commit -m "Agrega pruebas automatizadas de la parte G"
   ```

4. **Subir los cambios al repositorio remoto:**

   ```bash
   git push origin main
   ```

5. **El compañero actualiza su repositorio:**

   ```bash
   git pull origin main
   ```

6. **Ejecutar las pruebas:**

   ```bash
   pytest -v
   ```

7. **Verificar los resultados:**

   Comprobar que las pruebas se ejecuten correctamente en la computadora del compañero.

**Objetivo:** compartir los archivos de pruebas mediante GitHub y comprobar que otro integrante pueda descargarlos y ejecutarlos correctamente.