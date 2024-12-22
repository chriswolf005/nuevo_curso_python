class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible en este momento")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} fue devuelto")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no está disponible en este momento")
             
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no está en tu lista")


class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado correctamente")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido agregado correctamente")
    
    def books_available(self):
        print("Los libros disponibles son:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")


# Crear libros
book1 = Book("El Quijote de la Mancha", "Miguel de Cervantes")
book2 = Book("Dos pesos de agua", "Juan Bosch")

# Crear usuario
usuario1 = User("Carli", "001")

# Biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(usuario1)

# Realizar préstamo
usuario1.borrow_book(book1)

# Mostrar libros
library.books_available()

# Devolver libro
usuario1.return_book(book1)

# Mostrar libros nuevamente
library.books_available()
