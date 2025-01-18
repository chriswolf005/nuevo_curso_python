def log_transaction(func):
    def wrapper():
        print('1 log de la transaccion...')
        func()
        print('3 log terminado...')
    return wrapper


@log_transaction
def process_payment():
    print('2 Procesando pago... ')


process_payment()
