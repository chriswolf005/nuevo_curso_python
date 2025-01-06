"""
1)Recibira una lista de diccionarios
Cada diccionario tendra las claves:
"Nombre"."Edad" y "Sueldo".

2)Debe devolver una lista de empleados que ganen mas de cierto
sueldo.
"""

#Diccionario de empleados
empleados = {
    1: {"name": "Carlos", "age": 30, "salary": 200000.0},
    2: {"name": "Ana", "age": 25, "salary": 150000.0},
    3: {"name": "Luis", "age": 40, "salary": 250000.0},
    4: {"name": "Marta", "age": 28, "salary": 180000.0}
}

"""
Filtra empleados según una condición en un diccionario.

    :param empleados: Diccionario con la información de los empleados.
    :param clave: Clave sobre la cual aplicar la condición.
    :param condicion: Función para evaluar la condición.
    :return: Lista con los nombres de los empleados que cumplen la condición.
"""

def filtrar_empleados(empleados:dict,clave:str,condicion)->list:
    return[
        datos["name"]
        for datos in empleados.values()
        if clave in datos and condicion(datos[clave])
    ]


result=filtrar_empleados(empleados,"salary",lambda x:x>18000)
print(result)