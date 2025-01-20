"""
Crea dos decoradores:
saludar: Este decorador imprimirá "Hola, bienvenido!" antes de ejecutar cualquier función.
despedir: Este decorador imprimirá "¡Adiós, hasta luego!" después de ejecutar la función.
Aplica estos dos decoradores a una función llamada trabajar que solo imprima "Estoy trabajando...".
"""
def saludar(func):
    def wrapper(*args, **kwargs):
        print("Hola, bienvenido!")
        return func(*args, **kwargs)
    return wrapper

def despedir(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Ejecuta la función
        print("¡Adiós, hasta luego!")
        return result  # Devuelve el resultado de la función
    return wrapper

# Aplicando los decoradores anidados en el orden correcto
@saludar
@despedir
def trabajar():
    print("Estoy trabajando!")

# Llamando la función
trabajar()

