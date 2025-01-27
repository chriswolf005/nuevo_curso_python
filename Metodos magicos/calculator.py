def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multipli(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b

if __name__ == "__main__":
    print('Operaciones')
    res_1=suma(3,4)
    print(f'Suma: {res_1}')
    print(division(10,7))