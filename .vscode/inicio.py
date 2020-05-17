# Los comentarios de línea van con numeral.
''' Los comentarios de párrafo
van con las tres comillas '''
# Toda variable -> nombre sin espacio, sin símbolos especiales y coemnzar con una letra.
# Una variable que es de un tipo puede convertirse en una variable de otro tipo cualquiera.

edad = 25 # variable con un dato de tipo entero, =asignar
precio = 3443.25 # variable con un dato float (decimal)
nombre = "Fede" # variable con un dato de tipo caracter

total = edad + precio

print ("hola", nombre, "mi edad es:", edad)

num = int(input("Ingrese el primer número: "))

num2 = float(input("Ingrese el precio del producto: "))

articulo = input("Ingrese el nombre del producto: ")

print ("El nombre 1 elevado al cuadrado es ", num * num)

print("El producto ", articulo, "cuesta con IVA: $", num2 * 1.21)