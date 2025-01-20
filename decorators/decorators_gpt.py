"""
Crea un decorador llamado saludar.
Este decorador debe hacer lo siguiente:
Antes de ejecutar la función decorada, imprime "Hola, ¿cómo estás?".
Después de ejecutar la función decorada, imprime "Adiós, que tengas un buen día.".
Aplica el decorador a una función llamada presentarse que imprima el nombre de una persona.
"""
def saludar(func):
    def wrapper(name):
        print("Hola como estas?")
        func(name)
        print("Adios, que tengas buen dia")
    return wrapper



@saludar
def presentarse(name):
    print(f"Mi nombre es {name}")

presentarse("Chris")