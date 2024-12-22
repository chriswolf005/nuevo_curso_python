class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = False
    
    def encender(self):
        if not self.motor:
            self.motor = True
            print(f"El Auto {self.marca} {self.modelo} está encendido")
        else:
            print("El motor ya está encendido")
    
    def apagar(self):
        if self.motor:
            self.motor = False
            print(f"El Auto {self.marca} {self.modelo} se apagó")
        else:
            print("El motor ya está apagado")


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.vehiculos = []
    
    def comprar(self, auto):
        print(f"Hola {self.name}, ha comprado un nuevo carro {auto.marca} {auto.modelo}")
        self.vehiculos.append(auto)


class Consecionaria:
    def __init__(self):
        self.autos = []
        self.customers = []
    
    def add_auto(self, auto):
        self.autos.append(auto)
        print(f"El Auto {auto.marca} {auto.modelo} se agregó correctamente")
    
    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El Cliente {customer.name} ha sido agregado correctamente")
    
    def vender_auto(self, auto):
        if auto in self.autos:
            self.autos.remove(auto)
            print(f"El auto {auto.marca} {auto.modelo} ha sido vendido")
        else:
            print(f"El auto {auto.marca} {auto.modelo} no está en el inventario")
    
    def autos_available(self):
        print("Los Autos disponibles son:")
        for auto in self.autos:
            print(f" Marca: {auto.marca} Modelo: {auto.modelo}")


# Crear autos
auto1 = Auto("Toyota", "Corolla")
auto2 = Auto("Honda", "Civic")

# Crear cliente
cliente1 = Customer("Carlos", "001")

# Crear consecionaria
consecionaria = Consecionaria()
consecionaria.add_auto(auto1)
consecionaria.add_auto(auto2)
consecionaria.register_customer(cliente1)

# Realizar compra
cliente1.comprar(auto1)

# Mostrar autos disponibles
consecionaria.autos_available()

# Vender auto
consecionaria.vender_auto(auto1)

# Mostrar autos disponibles nuevamente
consecionaria.autos_available()
