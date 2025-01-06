animals=['Dog🐶','Cat😾','Fish🐟']

def print_animal(lista:list)-> str:
    for animal in lista:
        print(f"A {animal} would make a great pet")
    
    print("Any of this animals would make a great pet")

result1=print_animal(animals)