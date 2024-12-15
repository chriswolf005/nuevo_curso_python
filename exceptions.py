try:
    divisor=int(input("Ingresa un numero divisor-> "))
    result=100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero")
    print("Opss ha ocurrido un error",e)
except ValueError as e:
    print("Error:Debes introducir un numero valido")
    print("Opss ha ocurrido un error",e)