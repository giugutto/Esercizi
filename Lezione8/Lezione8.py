#Lezione 8
#EREDITARIETÀ E POLISMOSFIRMO

class Operazione:
    def __init__(self, operando) -> None:
        self.operando = operando

class OperazioneBinaria(Operazione):
    def __init__(self, operando, arg1, arg2) -> None:
        super().__init__(operando)
        self.arg1 = arg1
        self.arg2 = arg2
    #stiamo aggiungendo metodi alla sottoclasse operazionebinaria che prende l'attributo operando della superclasse
    def set_arg1(self,arg1): #setter
        self.arg1 = arg1

    def set_arg2(self, arg2): #setter
        self.arg2 = arg2

    def get_arg1(self): #getter
        return self.arg1
    
    def get_arg2(self): #getter
        return self.arg2
        
    def somma(self):
        return self.arg1 + self.arg2
    def esegui_operazione(self):
        if self.operando == '+':
            return self.somma()
        
    #il metodo statico prende degli input e eresituisce un output ma non accede agli attributi della classe
    #il metodo statico non accede allo stato dell'oggetto non avendo il self
    @staticmethod
    def static_sum(arg1: int, arg2:int):
        return arg1 + arg2
    def esegui_operazione(self):
        if self.operando == '+':
            return OperazioneBinaria.static_sum(self.arg1, self.arg2)
        
op = OperazioneBinaria('+', 5, 23)
#print(op.esegui_operazione())



from abc import *
# Exercise 1: Creating an Abstract Class with Abstract Methods

# Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.
#Le classi astratte sono dei template, dove una volta che crei la classe con i metodi che le sottoclassi devono ereditare
#esse non possorno farne a meno, ovvero se provi a fare un'istanza e non richiami tutte i metodi, python
#ti darà errore.
class Shape(ABC):
    @abstractmethod

    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass
        
class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def perimetro(self):
        return 2 * self.radius * 3.14
    
    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, base, altezza) -> None:
        self.base = base
        self.altezza = altezza

    def perimetro(self):
        return self.base * 2 + self.altezza * 2
    
    def area(self):
        return self.base + self.altezza
    
cerchio1 = Circle(12)
rettangolo1 = Rectangle(6,8)

print(cerchio1.perimetro())
print(cerchio1.area())
print(rettangolo1.perimetro())
print(rettangolo1.area())

# Exercise 2: Implementing Static Methods
books
# Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
# and another static method multiply that takes two numbers and returns their product.

class MathOperations:
    @staticmethod
    def add(num1, num2):
        return num1 + num2
    def moltiplica(num1, num2):
        return num1 * num2


print(MathOperations.add(1,2))
print(MathOperations.moltiplica(8,2))books


# Exercise 3: Library Management System 

# Create a Book class containing the following attributes: title, author, isbn
# The book class must contains the following methods:

#     __str__ method to return a string representation of the book.

#     @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". 
#It means that you must use the class reference cls to create a nebooksw object of the Book class using a string.

# Example: 

# book = “La Divina Commedia, D. Alighieri, 999000666”
# divina_commedia: Book = Book.from_string(book)
# Here divina_commedia must contain an instance of the class Book with 

# title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

class Book:
    def __init__(self, title, author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
#Il metodo str serve per ritornare una stringa quando proviamo a ritornare un oggetto

    def __str__(self):
        return (f"{self.title},{self.author},{self.isbn}")
    @classmethod
    def from_string(cls, book_str):
        title, author, isbn = book_str.split(', ')
        return Book(title, author, isbn)


# Create a Member class with the following attributes: name, member_id, borrowed_books
# The member class must contain the following methods:books

#     borrow_book(book) to add a book to the borrowed_books list.

#     return_book(book) to remove a book from the borrowed_books list.

#     __str__ method to return a string representation of the member.

#     @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".

class Member:
    def __init__(self, name, member_id) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrowed_book(self, book:Book):
        self.borrowed_books.append(book)

    def return_book(self, book:Book):
        self.borrowed_books.remove(book)

    def __str__(self) -> str:
        return (f"{self.name}, {self.member_id}")
    #il classmethod serve per chiamare le variabili di classe, quelle che troveremo sotto a class ma sopra il costruttore
    @classmethod
    def from_string(cls, member_str):
        name, member_id = member_str.split(", ")
        return Member(name, member_id)




# Create a Library class with the following attributes: books, members, total_books 
# (class attribute to keep track of the total number of books)
# The library class must contain the following methods:

#     add_book(book) to add a book to the library and increment total_books.

#     remove_book(book) to remove a book from the library and decrement total_books.

#     register_member(member) to add a member to the library.

#     lend_book(book, member) to lend a book to a member. 
#     It should check if the book is available and if the member is registered.

#     __str__ method to return a string representation of the library with the list of books and members.

#     @classmethod library_statistics(cls) to print the total number of books.

class Library:
    total_books = 0
    def __init__(self) -> None:
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)
        Library.total_books += 1 #quando andiamo a modificare la booksvariabile di classe, aggiungiamo il nome della classe, in questo caso "Library." e il nome della classe di  variabile

    def remove_book(self, book: Book):
        self.books.remove(book)
        Library.total_books -= 1

    def regist_member(self, member: Member):
        self.members.append(member)

    def lend_book(self, book, member: Member): #to lend a book to a member.
        if book in self.books and member in self.members:
            member.borrowed_book(book)
            Library.total_books -= 1
        else:books
            return "Libro mancante o membro non trovato"
    
    def __str__(self) -> str:
        return (f"I libri sono {self.books} e i membri sono {self.members}")
    @classmethod 
    def library_statistics(cls): #quando abbiamo un cls all'interno delle parentesi, possiamo richiamare la variabile della classe con "cls." Possiamo farlo con le funzioni e le variabili
        print(f"{cls.total_books}")

book: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book)
print(divina_commedia)

book = "The Communist Manifesto, Karl Marx, 555555555"
communist_manifesto: Book = Book.from_string(book)
print(communist_manifesto)
book = "The Iliad and The Odyssey, Homer, 713713713"
iliad_and_the_odyssey: Book = Book.from_string(book)
print(iliad_and_the_odyssey)

member: str = "Angelo Locarini, 666"
angelo: Member = Member.from_string(member)
member = "Ciro Immobile, 17"
Ciro: Member = Member.from_string(member)

library: Library = Library()
library.library_statistics()
library.add_book(divina_commedia)
library.add_book(communist_manifesto)
library.add_book(iliad_and_the_odyssey)

library.regist_member(angelo)
library.regist_member(Ciro)

library.library_statistics()
library.lend_book(communist_manifesto, angelo)
library.lend_book(divina_commedia, angelo)
library.library_statistics()
# Create a script and play a bit with the classes:
# Create instances of books and members using class methods. 
# Register members and add books to the library. 
# Lend books to members and display the state of the library before and after lending.