# Estructuras ciclicas
# Posibilidad de repetir una secuencia de código n cantidad de veces
# Ciclos tope fijo
 # condicion de corte

c = 1    # contador
mayores = 0     # contador de personas mayores de edad
s = 0    # inicializar sumador / acumulador en cero 0

while (c <= 4):
    edad = int(input("Ingrese edad: "))
    if (edad >= 18):
        mayores = mayores  + 1
    s = s + edad       # el dato a acumular en VARIABLE
   
    c = c + 1

print("El promedio de las edades es: ",s/4) 
prom = s/4   
print("El promedio de las edades es: ",prom)    
print("Cantidad de personas mayores de edad es: ", mayores)

