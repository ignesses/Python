# Estructuras ciclicas
# Posibilidad de repetir una secuencia de código n cantidad de veces
# Corte por cantidad de elementos ingresados previamente N
# Tope variable

c = 1
tope = int(input("Ingrese cantidad de elementos: "))

while(tope <= 0):   # la condicion es por el ERROR
    tope = int(input("Ingrese solo valores mayores a cero(0) : "))      # validacion

while(c <= tope):
    letra = input("Su letra: ")
    c = c + 1


