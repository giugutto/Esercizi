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
# Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
# and another static method multiply that takes two numbers and returns their product.

class MathOperations:
    @staticmethod
    def add(num1, num2):
        return num1 + num2
    def moltiplica(num1, num2):
        return num1 * num2


print(MathOperations.add(1,2))
print(MathOperations.moltiplica(8,2))


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
        else:
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




# Exercise 4: University Management System

# Create a system to manage a university with departments, courses, professors, and students. 

# Create an abstract class Person:
# Attributes:


# name (string)
# age (int)
# Methods:

# __init__ method to initialize the attributes.
# Abstract method get_role to be implemented by subclasses.
# __str__ method to return a string representation of the person.

class Person(ABC):
    def __init__(self, name:str,age:int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def get_roll(self):
        pass

    def __str__(self):
        return (f"{self.name},{self.age}")

        

# Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

# Student:
# Additional attributes: student_id (string), courses (list of Course instances)
# Method enroll(course) to enroll the student in a course.
class Student(Person):
    def __init__(self, name: str, age: int, student_id: str) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def get_roll(self):
        print("professor",self)
    

# Professor:
# Additional attributes: professor_id (string), department (string), courses (list of Course instances)
# Method assign_to_course(course) to assign the professor to a course.

class Professor(Person):
    def __init__(self, name: str, age: int, professor_id: str) -> None:
        super().__init__(name, age)
        self.professor_id = professor_id
        self.departement = Department
        self.courses = []

    def assign_to_course(self, course):
        self.courses.append(course)

    def get_roll(self):
        print("student",self)

    
# Create a class Course:
# Attributes:

# course_name (string)
# course_code (string)
# students (list of Student instances)
# professor (Professor instance)
# Methods:

# __init__ method to initialize the attributes.
# add_student(student) to add a student to the course.
# set_professor(professor) to set the professor for the course.
# __str__ method to return a string representation of the course.

class Course:
    def __init__(self, course_name: str, course_code: str) -> None:
        self.course_name = course_name
        self.course_code = course_code
        self.students: list[Student] = []
        self.professor = Professor
    
    def add_student(self, student: Student):
        self.students.append(student)

    def set_professor(self,professor: Professor):
        self.professor = professor
    
    def __str__(self) -> str:
        return (f"{self.course_name},{self.course_code},{self.students},{self.professor}")



# Create a class Department:

# Attributes:

# department_name (string)
# courses (list of Course instances)
# professors (list of Professor instances)

# Methods:

# __init__ method to initialize the attributes.
# add_course(course) to add a course to the department.
# add_professor(professor) to add a professor to the department.
# __str__ method to return a string representation of the department.

class Department:
    def __init__(self,department: str) -> None:
        self.department = department
        self.courses:list[Course]= []
        self.professor: list[Professor] = []

    def add_course(self, course:Course):
        self.courses = course

    def add_professor(self,professor:Professor):
        self.professor = professor
    def __str__(self):
        return (f"{self.department},{self.courses}, {self.professor}")
        
# Create a class University:

# Attributes:

# name (string)
# departments (list of Department instances)
# students (list of Student instances)

# Methods:

# __init__ method to initialize the attributes.
# add_department(department) to add a department to the university.
# add_student(student) to add a student to the university.
# __str__ method to return a string representation of the university.

class University:
    def __init__(self, name: str) -> None:
        self.name = name
        self.departments: list[Department] = []
        self.students: list[Student] = []
    def add_department(self, department: Department):
        self.departments.append(department)

    def add_student(self, student: Student):
        self.students.append(student)

    def __str__(self) -> str:
        message: str = f"\n{self.name.capitalize()} University\n\nDepartments:\n"
        message += '\n'.join(str(department) for department in self.departments)
        message += "\n\nStudents:\n"
        message += '\n'.join(str(student) for student in self.students)
        message += "\n"
        return message

# Create a script:

# Create instances of departments, courses, professors, and students.
# Add them to the university.
# Enroll students in courses and assign professors to courses.
# Display the state of the university.
# Create instances of departments, courses, professors, and students.
physics: Department = Department("physics")
engineering: Department = Department("engineering")
science: Department = Department("science and technology")

quantum: Course = Course("quantum physics", "p001")
relativity: Course = Course("relativity", "p002")
astro: Course = Course("astrophysics", "p003")
aerospace: Course = Course("aerospace engineering", "e001")
computer: Course = Course("computer engineering", "e002")
bio: Course = Course("bioengineering", "e003")
chem: Course = Course("chemistry", "s001")
math: Course = Course("mathematics", "s002")
geology: Course = Course("geology", "s003")

lupin: Professor = Professor("Remus Lupin", 38, "hgw001")
hagrid: Professor = Professor("Rubeus Hagrid", 54, "hgw002")
snape: Professor = Professor("Severus Snape", 38, "hgw003")
dyer: Professor = Professor("William Dyer", 33, "hpl0v3")
kirke: Professor = Professor("Digory Kirke", 61, "csl3w1s")
otto: Professor = Professor("Otto Liedenbrock", 42, "v3rn3")
moriarty: Professor = Professor("James Moriarty", 70, "c0n4nd0yl3")
langdon: Professor = Professor("Robert Langdon", 47, "t0mh4nk5")
keating: Professor = Professor("John Keating", 32, "d34dp03t5")

alfred: Student = Student("Alfred Hutheesing", 20, "std001")
freedon: Student = Student("Freedon Annunziato", 21, "std002")
alan: Student = Student("Alan Tucker", 19, "std003")
jenny: Student = Student("Jenny Coleman", 20, "std004")
yvonne: Student = Student("Yvonne William", 20, "std005")
eric: Student = Student("Eric Da Silva", 22, "std006")

# Add them to the university.
hailsmith: University = University("hailsmith")

# Enroll students in courses and assign professors to courses.
alfred.enroll(quantum)
alfred.enroll(computer)
alfred.enroll(math)
freedon.enroll(bio)
freedon.enroll(chem)
freedon.enroll(math)
alan.enroll(quantum)
alan.enroll(relativity)
jenny.enroll(bio)
jenny.enroll(geology)
jenny.enroll(astro)
yvonne.enroll(aerospace)
yvonne.enroll(astro)
yvonne.enroll(relativity)
eric.enroll(computer)
eric.enroll(quantum)
eric.enroll(math)

snape.assign_to_course(math)
lupin.assign_to_course(astro)
hagrid.assign_to_course(bio)
dyer.assign_to_course(relativity)
kirke.assign_to_course(chem)
moriarty.assign_to_course(quantum)
otto.assign_to_course(geology)
langdon.assign_to_course(computer)
keating.assign_to_course(aerospace)

physics.add_course(quantum)
physics.add_course(relativity)
physics.add_course(astro)
engineering.add_course(bio)
engineering.add_course(aerospace)
engineering.add_course(computer)
science.add_course(chem)
science.add_course(math)
science.add_course(geology)

physics.add_professor(dyer)
physics.add_professor(moriarty)
physics.add_professor(lupin)
engineering.add_professor(hagrid)
engineering.add_professor(keating)
engineering.add_professor(langdon)
science.add_professor(snape)
science.add_professor(kirke)
science.add_professor(otto)

hailsmith.add_department(physics)
hailsmith.add_department(engineering)
hailsmith.add_department(science)
hailsmith.add_student(alfred)
hailsmith.add_student(yvonne)
hailsmith.add_student(eric)
hailsmith.add_student(freedon)
hailsmith.add_student(alan)
hailsmith.add_student(jenny)

# Display the state of the university.
print(str(hailsmith))