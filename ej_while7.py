# Instrucción BREAK

i = 0

while (i < 7):
    print(i)
    if (i == 4):
        print("Saliendo del ciclo")
        break       # el flujo de control se interrumpe inmediatamente
    i = i + 1
