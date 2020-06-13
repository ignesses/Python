# diccionario con multiples values por clave

diccionario = {
                "Argentina":["Buenos Aires","Rosario","Mendoza","Cordoba"],
                "Peru":["Lima","Cuzco"],
                "Chile":"Santiago",
                "Brasil": ["Rio","Brasilia","Buzios"]
                }  # se puede asignar claves numericas y valores alfa y al reves

for pais in diccionario:        # recorrer el diccionario
   print(pais, ":", diccionario[pais])

print()
print(diccionario.items())  # devuelve en pares de diccionarios

print()
print(diccionario.keys())   # devuelve las keys

print()
print(diccionario.values())   # devuelve los valores

print()
print(len(diccionario))


for pais in diccionario:  
    if 'Cordoba' in diccionario[pais]:
       print("Existe")

print()
diccionario.clear()
print(diccionario)