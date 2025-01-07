from enum import Enum
from collections import deque

class DeliveryStatus(Enum):
    PENDING = 1      # Pendiente
    SHIPPED = 2      # Enviado
    DELIVERED = 3    # Entregado

class OrderManagement:
    def __init__(self):
        self.queue = deque()  # Cola para gestionar los pedidos

    def add_item(self, item):
        """Agregar un pedido al final de la cola."""
        self.queue.append(item)

    def add_left(self, item):
        """Agregar un pedido al inicio de la cola."""
        self.queue.appendleft(item)

    def remove_item(self):
        """Eliminar el último pedido."""
        if self.queue:
            return self.queue.pop()
        else:
            return "Queue is empty."

    def remove_left(self):
        """Eliminar el primer pedido."""
        if self.queue:
            return self.queue.popleft()
        else:
            return "Queue is empty."

    def get_items(self):
        """Obtener la lista de pedidos en la cola."""
        return list(self.queue)
    
    def remove_specific_item(self, item):
        """Remover un item específico."""
        if item in self.queue:
            self.queue.remove(item)
        else:
            return f"Item '{item}' not found in the queue."


    @staticmethod
    def check_order_status(status: DeliveryStatus):
        """Comprueba el estado del pedido y devuelve un mensaje."""
        if status == DeliveryStatus.PENDING:
            return "Order is still pending."
        elif status == DeliveryStatus.SHIPPED:
            return "Order has been shipped."
        elif status == DeliveryStatus.DELIVERED:
            return "Order has been delivered."
        else:
            return "Unknown status."


order_manager = OrderManagement()

# Agregar pedidos
order_manager.add_item("Order 1")
order_manager.add_item("Order 2")
order_manager.add_item("Order 3")

print("Current queue:", order_manager.get_items())  # ['Order 1', 'Order 2', 'Order 3']

# Eliminar un pedido específico
print(order_manager.remove_specific_item("Order 2"))  # "Item 'Order 2' removed successfully."
print("Current queue:", order_manager.get_items())  # ['Order 1', 'Order 3']

# Intentar eliminar un elemento inexistente
print(order_manager.remove_specific_item("Order X"))  # "Item 'Order X' not found in the queue."
