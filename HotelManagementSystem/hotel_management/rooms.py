# hotel_management/rooms.py
class Room:
    def __init__(self, room_number: int, room_type: str, price: float) -> None:
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True


class RoomManagement:
    def __init__(self) -> None:
        self.rooms = {}  # type: dict[int, Room]

    def add_room(self, room: Room) -> None:
        """Agrega una nueva habitación al sistema."""
        self.rooms[room.room_number] = room
        print(f"Habitación {room.room_number} agregada.")

    def check_availability(self, room_number: int) -> bool:
        """Verifica si una habitación está disponible."""
        room = self.rooms.get(room_number)
        if room and room.available:
            print(f"Habitación {room_number} está disponible.")
            return True
        print(f"Habitación {room_number} no está disponible.")
        return False
