class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand} {self.model} ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} {self.model} no está disponible")

    def check_available(self):
        return self.is_available

    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")


class Car(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} {self.model} está en marcha"
        else:
            return f"El coche no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no está disponible"


class Truck(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"El motor del Camión {self.brand} {self.model} está en marcha"
        else:
            return f"El Camión no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"El motor del Camión {self.brand} se ha detenido"
        else:
            return f"El Camión {self.brand} no está disponible"


class Moto(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"La Moto {self.brand} {self.model} está en marcha"
        else:
            return f"La Moto no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"La Moto {self.brand} se ha detenido"
        else:
            return f"La Moto {self.brand} no está disponible"


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
    
    def buy(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, el {vehicle.brand} {vehicle.model} no está disponible")
    
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(f"El {vehicle.brand} {vehicle.model} está {availability} y cuesta {vehicle.price}")


class Dealership:
    def __init__(self):
        self.vehicles = []
        self.customers = []
    
    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        print(f"El vehículo {vehicle.brand} {vehicle.model} se agregó correctamente")
    
    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido agregado correctamente")
    
    def vehicles_available(self):
        print("Los vehículos disponibles son:")
        for vehicle in self.vehicles:
            if vehicle.check_available():
                print(f" Marca: {vehicle.brand} Modelo: {vehicle.model}")


# Crear autos
auto1 = Car("Toyota", "Corolla", 20000)
auto2 = Truck("Ford", "F-150", 30000)
auto3 = Moto("Yamaha", "MT-07", 7500)
auto4=Truck("Changan","F-213",30000000)

# Crear cliente
cliente1 = Customer("Carlos")
cliente2=Customer("Robert")

# Crear concesionaria
concesionaria = Dealership()
concesionaria.add_vehicle(auto1)
concesionaria.add_vehicle(auto2)
concesionaria.add_vehicle(auto3)
concesionaria.register_customer(cliente1)
concesionaria.register_customer(cliente2)

# Mostrar vehículos disponibles antes de la venta
concesionaria.vehicles_available()

# Cliente compra un vehículo
cliente1.buy(auto1)


# Mostrar vehículos disponibles después de la venta
concesionaria.vehicles_available()

#Agregar un nuevo vehiculo
concesionaria.add_vehicle(auto4)

#Mostrar disponibles
concesionaria.vehicles_available()

#Comprar nuevo vehiculo
cliente2.buy(auto4)

#Mostrar vehiculos despues de venta
concesionaria.vehicles_available()