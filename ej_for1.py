# Comando FOR
#El bucle for se utiliza para recorrer los elementos de un objeto iterable 
# (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código.

for i in range(5): # va de 0 a 5, tope -1
    print("Python")

print ("****************************")

for num in range(1, 11, 2): # (minimo, maximo el max es -1, paso)
    print(num)

veces = int(input("¿Cuántas veces queres que te salude? "))
for i in range(veces):
    print("Hola !!")
    
print()
print("Adiós")