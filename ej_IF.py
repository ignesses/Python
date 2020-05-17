# Ejercicio con IF SIMPLE
# IF es un comando que nos permite establecer una condicion y actuar sobre ella: VERDADERA o FALSA

edad = int(input("Ingrese edad de la pesona: "))
precio1 = float(input("Ingrese el primer precio $"))
precio2 = float(input("Ingrese el segundo precio $ "))
leng = input("Ingrese que lenguaje de programación esta estudiando: ")

# Operadores de relación:  >  <  >=  <= == <> !=

if (edad >= 18):
    print("Es mayor")
else:
    print("NO es mayor de edad !")
    print("Vuelva cuando tenga 18 o mas")

if (precio1 < precio2):
    print("El primer precio es mas chico que el segundo")
 # else como parte del comando IF es NO obligatoria

if (leng == "Python"):
    print("Es el mejor lenguaje")
else:
    print("Ok, suerte !")

print ("Fin de ejercicio")

