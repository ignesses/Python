# importar funciones y modulos

import math
import ej_func_mat_import, ej_func_txt_import  # esta es la forma normal de llamar a un modulo

print(math.sqrt(24))

'''ej_func_mat_import.sumar(25,96)

ej_func_mat_import.dividir(52,9)

ej_func_txt_import.saludo("Curso de Python !!")'''

'''from ej_func_mat_import import sumar    # esta es la manera de llamar a una funcion específica

sumar(32,15)'''

from ej_func_mat_import import *  

# esta es la manera de llamar a todas las funciones definidas en el archivo, no es lo ideal
# por el tema de reservar memoria, es optimización, pero se usa mucho así.

restar(55,5)
