import sqlite3

# Gestor SQLite --> descargar
# crea un archivo en la carpeta donde este el archivo o donde fijemos
# conexion / creación a la base de datos

miConexion = sqlite3.connect("C:\Hernan\Clases 2020\Da Vinci - Python\Ejercicios\9-DB\SQLite\PrimeraBase")

miCursor=miConexion.cursor()    # creacion del puntero para ejecutar y manejar querys y sus resultados

# ejecuta una instrucción SQL
miCursor.execute("CREATE TABLE PRODUCTOS (nombre_articulo VARCHAR(50), precio REAL, seccion VARCHAR(20))")

miCursor.close()
miConexion.close()
