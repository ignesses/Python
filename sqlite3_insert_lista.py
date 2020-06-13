from conexion import *

variosProductos=[
        ("Camiseta",100,"Deportes"),
        ("Jarrón",70,"Casa"),
        ("Camión",100,"Jugueteria"),
        ("Mouse",430,"Tecnología"),
        ("Tarro",170,"Bazar"),
        ("Teclado",250,"Tecnología")
]                                    #   lista de articulos para insertar varios a la vez

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (null,?,?,?)",variosProductos)    # insertar lote de registros

miConexion.commit() # es la confirmación que quiero hacer esos cambios, es OBLIGATORIO

miConexion.close()
