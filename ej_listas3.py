# Algunas funciones para listas
numeros = [122,45,9,87,25]
milista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
nombres = ['Juan', 'Pedro', 'María', 'Andres', 'Carla']


# consultar si existe un elemento
if 'Pedro' in nombres:
    print("Existe", end=" ")

print()
# otra forma de mostrar las listas
for elem in milista:
    print(elem, end=" ")

print()
# ordenar listas
nombres.sort()

for elem in nombres:
    print(elem, end=" ")

print()
# extender listas
milista.extend(nombres)

for elem in milista:
    print(elem, end=" ")

print()
# eliminar un elemento por indice
nombres.pop(2)

for elem in nombres:
    print(elem, end=" ")

print()
# eliminar un elemento 
nombres.remove("Carla")

for elem in nombres:
    print(elem, end=" ")

print()
# dividir un texto caracter a caracter
texto= "Curso de Python"
lista = list(texto)
print(lista)
print(lista[9])

print()
# maximo elemento
print(max(numeros))
# minimo elemento
print(min(numeros))

