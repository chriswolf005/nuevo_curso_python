"""
Crea un progama de gestion de empleados

1) Funciones para **agregar** y **eliminar**
    empleados en una lista.


2) Un bloque `if __name__ ==
"__main__":` que permita probar
el funcionamiento del script ejecutandolo
directamente.
"""

empleados=[]

def add_employee(empleado):
    return empleados.append(empleado)

def delete_employee(empleado):
    if empleado in empleados:
        empleados.remove(empleado)
    else: print("Empleado no encontrado")
def list_employee():
    return print(empleados)


if __name__ == "__main__":
    print("Inicia el sistema")
    add_employee("Pedro")
    add_employee("juan")
    add_employee("maria")
    list_employee()
    delete_employee("maria")
    list_employee()

