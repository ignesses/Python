# Definicion de lista
# Funcion append, y funcion insert

numeros = []        # definir una lista
for i in range(3):
    nuevoDato = int(input( "Ingrese numero: " ))
    numeros.append(nuevoDato)   # ingresar un elemento a la lista

print(numeros[2])   # mostrar un elemento por separado, a partir de su posición

for i in range(0,len(numeros)):
    print (numeros[i] , end=" ")

numeros.insert(1,999)   # inserta un elemento en el indice o posicion indicada

print()

for i in range(0,len(numeros)):
    print (numeros[i] , end=" ")