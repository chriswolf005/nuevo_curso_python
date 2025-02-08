# hotel_management/customers.py
class Customer:
    def __init__(self, customer_id: int, name: str, email: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.email = email


class CustomerManagement:
    def __init__(self) -> None:
        self.customers = {}  # type: dict[int, Customer]

    def add_customer(self, customer: Customer) -> None:
        """Agrega un nuevo cliente al sistema."""
        self.customers[customer.customer_id] = customer
        print(f"Cliente {customer.name} agregado.")

    def get_customer(self, customer_id: int) -> str:
        """Obtiene la información de un cliente por ID."""
        customer = self.customers.get(customer_id)
        if customer is None:
            return "Cliente no encontrado."
        return f"Cliente: {customer.name}, Email: {customer.email}"
