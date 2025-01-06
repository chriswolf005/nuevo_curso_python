def divide(a:int,b:int)->float:
    #Validad que ambos parametros sean enteros
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("ambos parametros deben de ser enteros o flotantes")
        return None
    #Verificamos que el divisor no sea cero
    if b==0:
        raise ValueError("El divisor no puede ser cero")
       
    return a/b

#Ejemplo de uso

try:
    result=divide(10,'2') #Error de tipo
    print(result)
except TypeError as e:
    print(f"Error: {e}")

try:
    result=divide(10,0) #Error de division por cero
    print(result)
except ValueError as e:
    print(f"Error: {e}")
