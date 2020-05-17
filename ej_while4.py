# Corte por cantidad de elementos ingresados previamente N
# Tope variable
# Varios contadores

s = 0
c = 1
c_arg = 0   # contador para la cantidad de argentinos
c_otro = 0  # contador para la cantidad de otras nacionalidades

n = int(input("Cantidad de Apellidos:"))

while c<= n:
    apell = input("Ingrese Apellido:" )
    nac =input("Ingrese Nac:")
    if nac == "arg":
        c_arg = c_arg + 1
    else:
        c_otro = c_otro + 1
    c = c + 1

print ("La cantidad de argentinos son: ", c_arg, " y de otras nacionalidades ", c_otro)
    
    
    
