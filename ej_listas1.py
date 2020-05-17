# Una lista es una estructura de datos y un tipo de dato en python con características especiales.
# Te permite almacenar múltiples elementos en una sola variable.
# Lo especial de las listas en Python es que nos permiten almacenar cualquier tipo de valor como enteros y cadenas
# Son dinámicos en su longitud
# Se manejan con posiciones numericas, su indice es un numero, comienzan las lista con indice 0 (cero)

datos = [5,6,7,8,9,10]  # definicion de una lista
letras = ["A","B","C",22,"D",89,"otro"]

for i in range(0,6):
    print(datos[i])
    
print()

for i in range(0,len(letras)):   # len: cantidad de elementos de una lista
    print (letras[i] , end=" ")  # mostrar los items uno al lado del otro

print()