# definiamo una nuova classe!
class Persona:
    #il costruttore si crea così:(nome,cognome e codice fiscale sono attributi)
    def __init__(self, name:str , surname:str) -> None:
        #nb, ID non è stato messo nei parametri
        #mettiamo un underscore se vogliamo che gli attributi non vengano cambiati
        #per gli attributi privati un getter ritorna i valori(return, self.x) e setter consente di modificarle

        self._ID: int = 1
        self._name: str = name
        self._surname: str = surname
        self._birthdate: str = "12/03/2002"
        self._birth_place: str = "Napoli"
        self._gender: str = "M"
        self._ssn = None
        #funzioni della classe 
    def get_name(self):
        '''
        questa funziona stampa il nome della persona
        name: str
        return: self._name
        '''
        return self._name
    def setname(self, name:str) -> None:
        '''
        setter, this function seet the attribute name
        input: name : str, the paameter contains the user's name
        return: None
        '''
        raise Exception("You can't change the name!")
    def get_ssn(self) -> str:
        '''
        questa funzione legge il codice fiscale dell'utente
        tipo: str
        return: str
        '''
        return self._ssn 
    # def set_ssn(self, ssn: str) -> None:
    #     '''
    #     this function allow to set the ssn
    #     type:str
    #     return:str
    #     '''       
    #     self._ssn = ssn
    def set_ssn(self, ssn: str) -> None:
         '''
         this function allow to set the ssn
         type:str
         return:str
         '''       
    #raise Exception("you can't do it!")

    def compute_ssn(self) -> str:
        primelettere = "" 
        for i in self._name:
            if i in "bcdfghlmnpqrstvz":               
                primelettere += i
            else:
                continue
        first_three_character_name = primelettere[0] + primelettere[2] + primelettere[3]
        primeletterecognome = "" 
        for i in self._surname:
            if i in "bcdfghlmnpqrstvz":                               
                primeletterecognome += i
            else:
                continue
        first_three_character_surname = primeletterecognome[:3]
        year = self._birthdate[-2:]
        if self._birthdate[3:5] == "01":
            month = "A"
        elif self._birthdate[3:5] == "02":
            month = "B"
        elif self._birthdate[3:5] == "03":
            month = "C" 
        elif self._birthdate[3:5] == "04":
            month = "D" 
        elif self._birthdate[3:5] == "05":
            month = "E"
        elif self._birthdate[3:5] == "06":
            month = "H"
        elif self._birthdate[3:5] == "07":
            month = "L"
        elif self._birthdate[3:5] == "08":
            month = "M" 
        elif self._birthdate[3:5] == "09":
            month = "P" 
        elif self._birthdate[3:5] == "10":
            month = "R" 
        elif self._birthdate[3:5] == "11":
            month = "S"
        elif self._birthdate[3:5] == "12":
            month = "T" 
        day = self._birthdate[:2]
        if self._gender == "F":
            day = self._birthdate[:2] + 40
        elif self._birth_place == "L'aquila":
            city = "A345" 
        elif self._birth_place == "Ancona":
            city = "A271"       
        elif self._birth_place == "Aosta":
            city = "A326" 
        elif self._birth_place == "Bari":
            city = "A662"
        elif self._birth_place == "Bologna":
            city = "A944" 
        elif self._birth_place == "Cagliari":
            city = "B354"    
        elif self._birth_place == "Campobasso":
            city = "B519" 
        elif self._birth_place == "Catanzaro":
            city = "C352"       
        elif self._birth_place == "Firenze":
            city = "D612" 
        elif self._birth_place == "Genova":
            city = "D969"       
        elif self._birth_place == "Milano":
            city = "F205"
        elif self._birth_place == "Napoli":
            city = "F839"
        elif self._birth_place == "Palermo":
            city = "G273"
        elif self._birth_place == "Perugia":
            city = "G478"
        elif self._birth_place == "Potenza":
            city = "G942"
        elif self._birth_place == "Roma":
            city = "H501"
        elif self._birth_place == "Torino":
            city = "L219"
        elif self._birth_place == "Trento":
            city = "L378"
        elif self._birth_place == "Trieste":
            city = "L424"
        elif self._birth_place == "Venezia":
            city = "L736"

        self._ssn = first_three_character_surname.upper() + first_three_character_name.upper() + year + month + day + city




#andiamo a creare oggetto/istanza
persona_1: Persona = Persona(name="giuseppe", surname="guttoriello",)
persona_1.compute_ssn()
print(persona_1.get_ssn())


#persona_1.setname(name="peppe")

#print(persona_1.get_name())

# persona_2: Persona = Persona(name="Valentino", surname="Rossi", ssn="VLTRSS")
# persona_2.set_ssn("HFISDJD")
# print(persona_2.get_ssn())
# queue: list[Persona] = [persona_1,persona_2]
# for i in queue:
#     print(i.get_cf())

#esercizio1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice", 45)
bob = Person("bob", 36)

print(alice.age)
print(bob.age)
#esercizio2

class Student:
    def __init__(self, name:str, studyProgram:str, age: int, gender: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def print_info(self):
        return self.name, self.studyProgram, self.age, self.gender

persona1 = Student("Giuseppe","cybersecurity", 27, "m")
person2 = Student("Gabriele", "FullStack", 26, "m")
person3 = Student("Angelo", "Cloud-developer", 19, "m")

print(person3.print_info())

#esercizio3

class Animal:
    def __init__(self, name:str, legs:int):
        self.name = name
        self.legs = legs

    def setLegs(self, newleg):
        self.legs = newleg
    
    def getLegs(self):
        return self.legs
    

    def print_info1(self):
        return self.name, self.legs

animal1 = Animal("Cane", 4)
animal2 = Animal("Elefante", 4)

animal1.setLegs(3)

print(animal1.legs)
print(animal1.getLegs())
print(animal1.print_info1())


dizionario = {"valore1":5}
print(dizionario["valore1"])

#esercizio4

class Food:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

food1 = Food("Hotdog", 3.50, " è popo bono")
food2 = Food("Tramezzino", 2.50, " è popo bono se ce sta er pomodoro e il tonnazzo")
food3 = Food("Gelato", 3.50, " è popo bono, sopratutto co i gusti zabaione e il cioccolato all'arancia")

class Menu:
    def __init__(self, foods = []) -> None:
        self.foods = foods
    def addfood(self, af: Food):
        self.foods.append(af)
    def removefood(self, rf:Food):
        self.foods.remove(rf)
    def printprices(self):
        for i in self.foods:
            print(i.price) 
    def getAveragePrice(self):
        v = 0
        for i in self.foods:
            v += i.price
        print(v / 5)           
    
    
food4 = Food("Bigmac", 4.60, "panino enorme molto buono")
food5 = Food("Cornetto", 0.60, "se alla cioccolata buonissimo")
menu = Menu()

menu.addfood(food1)
menu.addfood(food2)
menu.addfood(food3)
menu.addfood(food4)
menu.addfood(food5)

menu.printprices()
menu.getAveragePrice()
