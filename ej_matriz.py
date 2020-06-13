nombres = ['Juan', 'Pedro', 'María', 'Andres', 'Carla','Esteban']
apellidos = ['Perez', 'Martinez', 'Rodriguez', 'Alvarado', 'Estefano','Romano']

matriz = [nombres,apellidos]
i = 0
print(matriz)
print(len(matriz))
print(len(matriz[i]))

print("Nombres"," Apellidos")
for j in range(len(matriz[i])):
    print(matriz[i][j],"\t",matriz[i+1][j], end='\n')