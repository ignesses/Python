# concatenar
mensaje1 = 'Hola' + ' ' + 'Mundo'
print(mensaje1)

# multiplicar
mensaje2a = 'Hola ' * 3
mensaje2b = 'Mundo'
print(mensaje2a + mensaje2b)

# añadir
mensaje3 = 'Hola'
mensaje3 += ' '
mensaje3 += 'Mundo'
print(mensaje3)

# longitud, el espacio cuenta como caracter
mensaje4 = 'Curso' + ' de ' + 'Python'
print(len(mensaje4))

# encontrar, indica el indice de inicio de lo encontrado, desde el caracter 0, si no la encuentra -1
mensaje5 = "Curso de Python CUVL"
mensaje5a = mensaje5.find("Python")
mensaje5b = mensaje5.find("Hoy")
print(mensaje5a)
print(mensaje5b)

# reemplazar
mensaje8 = "Curso de Python CU"
mensaje8a = mensaje8.replace("CU", "CUVL")
print(mensaje8a)

# extraer
mensaje9 = "Curso de Python"
mensaje9a = mensaje9[1:4]
mensaje9_b = mensaje9[3:]
print(mensaje9a)
print(mensaje9_b)

# secuencia de escape
print('El programa imprime \"Hola Mundo\"')

# separa en una lista
mensaje10 = "Curso de Python CUVL"
mi_lista = mensaje10.split()
print(mi_lista)
