def log_employee_action(func):
    def wrapper(*args, **kwargs):
        action_log = f"Acción realizada: {func.__name__}, argumentos: {args}, {kwargs}\n"
        with open('logprogram.txt', 'a') as file:  # Modo 'a' para agregar registros
            file.write(action_log)
        result = func(*args, **kwargs)  # Ejecutar la función original
        return result
    return wrapper

@log_employee_action
def ejecutar_system(text):
    print(f"El log se guardó en el archivo llamado {text}")

@log_employee_action
def realizar_otra_accion(empleado, accion):
    print(f"El empleado {empleado} realizó la acción: {accion}")

# Ejecución
text = 'logprogram.txt'
ejecutar_system(text)

realizar_otra_accion("Juan", "Actualizar datos de cliente")
realizar_otra_accion("Ana", "Eliminar registro")
