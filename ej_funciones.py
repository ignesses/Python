# Funciones de usuario
# Una función es una porción o bloque de código reutilizable
# que se encarga de realizar una determinada tarea y puede ser
# llamado las veces que sea necesario y hacer que el cogido sea
# mas legible y ordenado

def mensaje():   # definicion de funcion
    print ("Hola al curso !!")
    
mensaje()   # llamada o invocación a la función
print ("Esto esta fuera de funcion")
mensaje()


def suma():
    num1 = 23   # locales a la funcion, es decir privadas al resto del programa
    num2 = 24
    print (num1+ num2)

suma()

def sumap(n1, n2):  # con pasajes de parámetros
    print (n1 + n2)

sumap(55,23)  
sumap(5,2)  # con pasajes de parámetros

def suma(num1, num2):
    resul = num1  + num2
    return resul

print(suma(5.6,68))

resultado_funcion = suma(78,23) # alcenamiento del resultado de la funcion en una variable
print (resultado_funcion)

if resultado_funcion > 100:
    print("No corresponde")