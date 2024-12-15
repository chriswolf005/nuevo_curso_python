def add(a,b):
    return a+b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide (a,b):
    return a/b

def calculator():
    while True:
        print("Seleccione una opcion")
        print("1 suma")
        print("2 resta")
        print("3 Multiplicacion")
        print("4 division")
        print("5 cerrar")

        option=input("Ingresa tu opcion: ")

        if option =="5":
            print("Good Bye!")
            break
        if option in ["1","2","3","4"]:
            num1=float(input("Ingresa tu primer numero: "))
            num2=float(input("Ingresa tu segundo numero: "))

            if option=="1":
                print("El resultado de la suma es", add(num1,num2))
            elif option=="2":
                print("El resultado de la resta es", substract(num1,num2))
            elif option=="3":
                print("El resultado de la multiplicacion es", multiply(num1,num2))
            elif option=="4":
                print("El resultado de la division es", divide(num1,num2))
        else:
            print("Opcion no valida por favor intente nuevamente")
calculator()