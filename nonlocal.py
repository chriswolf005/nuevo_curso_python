def outer_function():
    x='enclosing'
    
    def inner_function():
        nonlocal x
        x='modifed'
        print(f'El valor es inner es: {x}')
    inner_function()
    print(f'El valor outer: {x}')
outer_function()