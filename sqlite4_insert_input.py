''' A partir de Python 3.6 las cadenas f proporcionan una forma fácil de integrar
variables y expresiones dentro de una cadena empleando una sintaxis muy reducida. 

Insertar registros en la tabla por medio de input'''

from conexion import *

modelo = 'HP I7'
precio = 65000
impuestos = precio * 21/100
print(f'Notebook {modelo}: {precio+impuestos} pesos')

nombres = []
precios = []
secciones = []

for i in range(2):
    nom = input("Nombre: ")
    precio = float(input("Precio: "))
    seccion = input("Sección :")
    nombres.append(nom)
    precios.append(precio) 
    secciones.append(seccion) 

i=0
while i < len(nombres):
   miCursor.execute(f'INSERT INTO PRODUCTOS VALUES (null, "{nombres[i]}","{precios[i]}","{secciones[i]}")')
   i = i+1
   
miConexion.commit()

miConexion.close()
