x='global'#Es una variable global

#Funcion externa
def outer_function():
    x='enclosing'
    #Funcion interna
    def inner_function():
        x='Local'#Variable local
        print(x)
    
    inner_function()
    print(x)

outer_function()
print(x)