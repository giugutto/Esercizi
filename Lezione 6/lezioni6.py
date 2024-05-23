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

##############################################################################################################
# 9-1. Restaurant: Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name,cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant_name(self):
        print(f"Nome ristorante: {self.restaurant_name}, Tipo di cucina: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
    
    def set_number_served(self, new_number):
        self.number_served = new_number
    
    def increment_number_served(self, add_number):
        self.number_served = self.number_served + add_number


ristorante1 = Restaurant("All italy", "Italiana")
ristorante1.describe_restaurant_name()
ristorante1.open_restaurant()
#Add a method called increment_number_served() 
# that lets you increment the number of customers who’ve been served. 
#Add a method called set_number_served() that lets you set the number of customers that have been served
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. 
# Create three different instances from the class, 
# and call describe_restaurant() for each instance.
ristorante2 = Restaurant("Spicy and else", "Messicana")
ristorante3 = Restaurant("Kali's House", "Indiana")
ristorante4 = Restaurant("Chin Chong", "Cinese")

ristorante2.describe_restaurant_name()
ristorante3.describe_restaurant_name()
ristorante4.describe_restaurant_name()

# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name,
#  and then create several other attributes that are typically stored in a user profile.
#  Make a method called describe_user() that prints a summary of the user’s information.
#  Make another method called greet_user() that prints a personalized greeting to the user.
#  Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name, age, height, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"Name: {self.first_name},Last name: {self.last_name}, Age: {self.age},Height: {self.height}")

    def greet_user(self):
        print(f"Good morning {self.first_name}")
    
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Write a method called increment_login_attempts() that increments the value of login_attempts by 1
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
# user1 = User("Marco", "Finestrelli", 16, 1.67)
# user2 = User("Valerio", "Finestrelli", 16, 1.71)
# user3 = User("Giada", "Galetti", 22, 1.68)
# user4 = User("Valentina", "Mastari", 34, 1.70)

# user1.describe_user()
# user2.describe_user()
# user3.describe_user()
# user4.describe_user()

# 9-4. Number Served: Start with your program from Exercise 9-1.
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served, and then change this value and print it again. 
# Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again. Add a method called increment_number_served() 
# that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in,
# say, a day of business. 
restaurant = Restaurant("mai na gioia","Polacca", 34)
print(restaurant.number_served)
restaurant.set_number_served(56)
print(restaurant.number_served)
restaurant.increment_number_served(52)
print(restaurant.number_served)

# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, 
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
user5 = User("Sandro","Fantaino",56,181,23)

user5.increment_login_attempts()
user5.increment_login_attempts()
user5.increment_login_attempts()
user5.increment_login_attempts()
user5.increment_login_attempts()
print(user5.login_attempts)

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4.
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method. 

class IcecreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavour = [], number_served=0):
        #qui sopra aggiungiamo gli attributi che ci servono di questa sottoclasse
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavour = flavour

    def display_flavour(self):
        print(self.flavour)

gelateria = IcecreamStand("Gelatazzo","gelateria",["Pistacchio","Zabaione","Arancia"], 14)

gelateria.display_flavour()

# 9-7. Admin: An administrator is a special kind of user.
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5.
#  Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user",
#  and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. 
#  Create an instance of Admin, and call your method. 

class Admin(User):
    def __init__(self, first_name, last_name, age, height, login_attempts, privileges = []):
        super().__init__(first_name, last_name, age, height, login_attempts)
        self.privileges = privileges
    

Amministratore = Admin("Mirka","Santoni",23, 1.72, 12,["Can add post","Can delete post","Can ban user","Can change name of user"])

#Amministratore.show_privileges()

# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, 
# that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, age, height, login_attempts, privileges:Privileges):
        super().__init__(first_name, last_name, age, height, login_attempts)
        self.privileges = privileges

privilegi1 = Privileges(["Can add post","Can delete post","Can ban user","Can change name of user"])
Amministratore1 = Admin("Pippo","Franco",32,1.67,6,privilegi1)

Amministratore1.privileges.show_privileges()

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
#  Make a separate file that imports Restaurant. 
# Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

