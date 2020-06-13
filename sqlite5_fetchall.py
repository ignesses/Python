from conexion import *
from consultas import *

lista = miCursor.execute(todos_reg)
lista = miCursor.fetchall() 

for producto in lista:
        print ("Articulo: ", producto[0], " / Nombre: ", producto[1]) 

lista = miCursor.execute("SELECT * FROM PRODUCTOS WHERE precio >= 350")
lista = miCursor.fetchall()       # asigna el contenido a un arreglo

print("\nSolo los productos de $ 350 en adelante\n")  

for producto in lista:
        print ("Articulo: ", producto[0], " / Precio: ", producto[2]) 

# con ingreso del dato

dato = float(input("A partir de que precio: "))

lista = miCursor.execute(f"SELECT * FROM PRODUCTOS WHERE precio >= '{dato}'")

lista = miCursor.fetchall() 

print(lista)

miConexion.close()