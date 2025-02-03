import multiprocessing

#Funcion que calcule el cuadrado de un número
def square(n):
    return n ** 2

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    #Crear un nuevo proceso
    with multiprocessing.Pool() as pool:
        #Aplicar la función a cada elemento de la lista
        result = pool.map(square, numbers)

    print(f"Resultados {result}")
