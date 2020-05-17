# Ejercicio con IF CON CONECTORES LOGICOS: ellos son el Y and y el O OR

edad = int(input("Ingrese la edad: "))
pais = input("Ingrese pais: ")

if (edad >=18 and edad <=65):
    print("Activo")
else:
    print("Revisar")

if (edad >=50 and pais == "Italia"):
    print("Alto riesgo !!")

if (edad >=50 or pais == "Italia"):
    print("Altisimo riesgo !!")