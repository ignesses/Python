import sqlite3

miConexion = sqlite3.connect("C:\Hernan\Clases 2020\Da Vinci - Python\Ejercicios\9-DB\SQLite\PrimeraBase")
miCursor=miConexion.cursor()    # creacion del puntero

miCursor.execute("INSERT INTO PRODUCTOS VALUES('Pelota',500,'Deportes')")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('Birome',30,'Libreria')")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('notebook',15000,'IT')")

miConexion.commit() # es la confirmación que quiero hacer esos cambios, es OBLIGATORIO

miConexion.close()