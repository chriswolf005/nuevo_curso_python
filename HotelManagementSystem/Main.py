# main.py
import asyncio
from datetime import datetime
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment


async def main():
    # Inicializar sistemas de gestión
    reservation_system = ReservationSystem()
    customer_management = CustomerManagement()
    room_management = RoomManagement()

    # Agregar habitaciones
    room_management.add_room(Room(101, "Single", 100))
    room_management.add_room(Room(102, "Double", 150))

    # Agregar clientes
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer_management.add_customer(customer1)

    customer2 = Customer(2, "Bob", "bob@example.com")
    customer_management.add_customer(customer2)

    # Procesar la reserva y el pago para la habitación 101 (Alice)
    if room_management.check_availability(101):
        reservation = Reservation(1, "Alice", 101, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)
        await process_payment("Alice", 100)

    # Procesar la reserva y el pago para la habitación 102 (Bob)
    if room_management.check_availability(102):
        reservation = Reservation(2, "Bob", 102, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)
        await process_payment("Bob", 150)


if __name__ == "__main__":
    asyncio.run(main())
