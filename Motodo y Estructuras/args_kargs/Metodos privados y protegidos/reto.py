"""
Implementa una clase CuentaBancaria con un metodo
protegido para actualizar el saldo de la cuenta.
metodo privado para registrar las transacciones
internamiente.

1.El metodo protegido (_actualizar_saldo) debe ser 
utilizado dentro de la clase y suss subsclases

2.El metodo privado (_registrar_transaccion) debe ser
completamente interno y no accesible fuera de la clase.



"""
class CuentaBancaria:
    # Método privado para registrar transacciones
    def __registrar_transaccion(self, tipo, monto):
        # Guarda la transacción en una lista privada con el tipo y monto
        self.__transacciones.append({"tipo": tipo, "monto": monto})

    # Método protegido para actualizar el saldo
    def _actualizar_saldo(self, monto):
        self._saldo += monto  # Modifica el saldo de la cuenta

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial
        self.__transacciones = []  # Lista privada para registrar las transacciones

    def depositar(self, monto):
        # Si el monto es positivo, actualizamos el saldo y registramos la transacción
        if monto > 0:
            self._actualizar_saldo(monto)  # Llama al método protegido para actualizar el saldo
            self.__registrar_transaccion("Depósito", monto)  # Llama al método privado para registrar la transacción
            print(f"Querido cliente {self.titular}, le informamos que se acaba de agregar {monto} en su cuenta de forma exitosa.")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        # Verificamos que el monto sea válido y suficiente para realizar el retiro
        if 0 < monto <= self._saldo:
            self._actualizar_saldo(-monto)  # Disminuye el saldo usando el método protegido
            self.__registrar_transaccion("Retiro", monto)  # Registra la transacción como privada
            print(f"Querido cliente {self.titular}, le informamos que se ha retirado {monto} de su cuenta de forma exitosa.")
        else:
            print("Fondos insuficientes o monto inválido.")

    def mostrar_saldo(self):
        # Muestra el saldo actual de la cuenta
        print(f"Saldo actual: {self._saldo}")

    def mostrar_transacciones(self):
        # Muestra el historial de transacciones almacenadas de forma privada
        print("Historial de transacciones:")
        for transaccion in self.__transacciones:
            print(transaccion)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la cuenta bancaria
    cuenta = CuentaBancaria("Christopher", 1000)
    
    # Mostrar el saldo inicial
    cuenta.mostrar_saldo()
    
    # Realizar un depósito y mostrar el saldo actualizado
    cuenta.depositar(500)
    
    # Realizar un retiro y mostrar el saldo actualizado
    cuenta.retirar(300)
    
    # Mostrar el historial de transacciones
    cuenta.mostrar_transacciones()

