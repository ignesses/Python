# Diccionarios
# Los diccionarios en Python son un tipo de estructuras de datos que permite guardar
# un conjunto no ordenado de pares clave-valor, siendo las claves únicas dentro 
# de un mismo diccionario (es decir que no pueden existir dos elementos con una misma clave).
# Es similar en otros lenguajes a un array asociativo

telefonos = {
    'juan':  3453454,
    'maria': 7435551,
    'pedro': 4344567,
}

print(telefonos)
# los valores se extraen a traves de las keys(llaves)
print(telefonos['juan'])

del telefonos['maria']   # borrar un elemento
print(telefonos)

# para asignar un nuevo elemento, si esta mal la puedo sobre escribir
telefonos["carolina"] = 658471 
print(telefonos)

print(telefonos.keys())
print(telefonos.values())

if 'juan' in telefonos:
    print("Existe!!") 

for elem in telefonos:
    print(elem,telefonos[elem])