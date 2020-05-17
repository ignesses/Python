# Ejercicio con IF COMBINADO / anidado / IF dentro de IF
# Se utiliza cuando tenemos más de 2 posibles salidas
# Cantidad de IF a usar = cantidad de salidas necesarias - 1

precio1 = float(input("Ingrese el primer precio $"))
precio2 = float(input("Ingrese el segundo precio $ "))

if (precio1 > precio2):
    print("El primer precio es mayor")
else:
    if (precio2 > precio1):
        print("El segundo precio es mayor")
    else:
        print("Son iguales !!")