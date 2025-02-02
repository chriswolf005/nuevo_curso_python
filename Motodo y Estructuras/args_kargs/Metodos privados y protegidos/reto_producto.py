"""
Implementa la clase Producto:

1. Utiliza @property para controlar el acceso 
y modificación y acceso del precio.
"""

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("No se aceptan valores negativos")
        self.__precio = valor
    
    @precio.deleter
    def  precio(self):
        print(f"El precio del producto {self.nombre} ha sido eliminado")
        del self.__precio


pan=Producto("Pan", 0.5)
#print(pan.precio)
pan.precio=6
print(pan.precio)
#pan.precio=-1
del pan.precio