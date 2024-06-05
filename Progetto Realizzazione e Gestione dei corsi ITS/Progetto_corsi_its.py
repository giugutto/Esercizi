""" In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
### Classe Room:
La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area). 
L'area è calcolata come il doppio dei posti.
- Metodi:
    - get_id(): Restituisce l'ID dell'aula.
    - get_floor(): Restituisce il piano dell'aula.
    - get_seats(): Restituisce il numero di posti dell'aula.
    - get_area(): Restituisce l'area dell'aula. """

class Room:
    def __init__(self, id: int, floor: int, seats: int):
        self.id = id
        self.floor = floor
        self.seats = seats
      

    def get_id(self):
        return self.id
    
    def get_floor(self):
        return self.floor
    
    def get_seats(self):
        return self.seats
    
    def get_area(self) -> int:
        return self.seats * 2
    
class Building:
    def __init__(self, name:str, address: str, floors: int):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms: list[Room] = []

    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
    
    def add_room(self, room: Room):
        if min(self.floors) <= room.floor <= max(self.floors):
            if room not in self.rooms:
                self.rooms.append(room)

    def area(self):
        area = 0
        for room in self.rooms:
            area += room.get_area()
        return area



class Person:
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
        self.group = None
class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        super().__init__(cf, name, surname, age)
        self.group = None


    def set_group(self, group):
        self.group = group
        
class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        super().__init__(cf, name, surname, age)




class Group:
    def __init__(self, name: str, limit:int):
        self.name = name
        self.limit = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []


    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
       num_student = len(self.students)
       num_prof = num_student // 10 + 1
       return num_prof
    
    def add_student(self, student:Student):
        if len(student) +1 < self.limit:
            if student not in self.students:
                self.students.append(student)
        
    def add_lecturer(self, lecturer: Lecturer):
        if len(lecturer) + 1 < self.get_limit_lecturers():
            if lecturer not in self.lecturers:
                self.lecturers.append(lecturer)



class Person:
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
        self.group = None
    
class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        super().__init__(cf, name, surname, age)
        
    def set_group(self, group):
        self.group = group
        
class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        super().__init__(cf, name, surname, age)




class Group:
    def __init__(self, name: str, limit:int):
        self.name = name
        self.limit = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []


    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
       num_student = len(self.students)
       num_prof = num_student // 10 + 1
       return num_prof
    
    def add_student(self, student:Student):
        if len(self.students) +1 <= self.limit:
            if student not in self.students:
                self.students.append(student)
        
    def add_lecturer(self, lecturer: Lecturer):
        if len(self.lecturers) + 1 <= self.get_limit_lecturers():
            if lecturer not in self.lecturers:
                self.lecturers.append(lecturer)


class Course:
    def __init__(self, name: str):
        self.name = name
        self.groups: list[Group] = []

    def register(self, student):
        for group in self.groups:
            if len(group.students) < group.limit:
                group.students.append(student)
                break
        

    def get_groups(self):
        return self.groups
    
    def add_group(self, group):
        self.groups.append(group)



'''
Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) 
e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi,
 aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, 
stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. '''

class Media:
    def __init__(self, title: str) -> None:
        self.title = title
        self.reviews: list[int] = []


    def set_title(self, title):
        self.title = title
        
    def get_title(self):
        return self.title
    
    def aggiungi_valutazione(self, voto):
        self.reviews.append(voto)
        
    

Esempio di riassunto: 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film,
 aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione(). '''



