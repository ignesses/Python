'''Como sucede con un diccionario convencional, un diccionario en Python 
es una palabra que tiene asociado algo. Al contrario de lo que sucedía en las listas, 
los diccionarios no tienen orden.
Se crean poniendo sus elementos entre llaves {"a":"Argentina", "b":"Barcelona",>>>}.
Se denominan keys a las «palabras» y values a las «definiciones».
Lógicamente, no puede haber dos keys iguales, aunque sí dos values iguales. '''

diccionario = {'Piloto 1':'Fernando Alonso', 'Piloto 2':'Kimi Raikkonen', 'Piloto 3':'Felipe Massa'}
print(diccionario)
print(diccionario['Piloto 2'])

 # get(): Devuelve el valor que corresponde con la key introducida.
print(diccionario.get('Piloto 1'))

 # pop(): Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
print(diccionario.pop('Piloto 1'))
print(diccionario)

 # update(): Actualiza el valor de una determinada key o lo crea si no existe.
diccionario.update({'Piloto 4':'Lewis Hamilton'})
diccionario.update({'Piloto 2':'Sebastian Vettel'})
diccionario["Piloto 5"] = "Valtteri Bottas"
print(diccionario)

 # "key" in diccionario: devuelve verdadero (True) o falso (False) si la key existe en el diccionario.
print ("Piloto 1" in diccionario)

print ("Piloto 2" in diccionario)

print ("Sebastian Vettel" in diccionario)

# devuelve verdadero (True) o falso (False) si la definición existe en el diccionario.
print ("Sebastian Vettel" in diccionario.values())
