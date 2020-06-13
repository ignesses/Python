# Ir a CMD, escribir Python, luego help(), y finalmente modules

import math, random, calendar

m1 = math.pow(2, 5) # 2 elevado a la 5ta potencia
m2 = math.sqrt(4) # Raíz cuadrada de 4
m3 = math.cos(2*math.pi) # Coseno del ángulo de 2*pi radianes (180°).

print(m1)
print(m2)
print(m3)

azar = random.randint(1,20)
print (azar)

#Instancia de TextCalendar
cl = calendar.TextCalendar(firstweekday=0)

#Elegimos el formato del año y mes del calendario
calendario_may = cl.formatmonth(2020, 5)

#Mostramos el resultado
print(calendario_may)
