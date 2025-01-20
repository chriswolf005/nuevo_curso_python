#Decorador que comprueba si un empleado tiene un rol especifico
def check_access(role):
    def decorator(func):
        def wrapper(employee):
            #Si el rol del empleado coincide con el rol requerido
            if employee.get('role')==role:
                return func(employee)
            else:
                print("Acceso denegado loco mio🤖")
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Se registra accion del empleado {employee['name']}')
        return func(employee)
    return wrapper

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado')


admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

#delete_employee(admin)
delete_employee(employee)
