# Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
# The function should return a dictionary with the playlist name and a set of songs. 
# Call the function with different numbers of songs to demonstrate flexibility.
# Example: create_playlist("Road Trip", {"Song 1", "Song 2"})
# Write a function called add_like() that accepts a dictionary, 
# the name of a playlist, and a boolean value indicating whether it is liked (True or False).
# This function should return an updated dictionary.
# Example: add_like(dictionary, “Road Trip”, liked=True)
def create_playlist(name:str,songs:set):
    return name,songs

print(create_playlist("ciccio",{"al mio volo, ciccio"}))


def add_like(dizionario:dict, name:str, liked:bool):
    x = (f"Liked={liked}")
    
    return dizionario,name,x

print(add_like({"v_1":"ciao"},"canzone", True))    

# 2. Book Collection:

# Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
# This function should return a dictionary where the author's name is the key and the value is a list of their books. 
# Demonstrate this function by adding books for different authors.
# Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
def add_book(name:str,titoli:list):
    return {name:[titoli]}

print(add_book("ciccio",["ciao","cioa"]))


# Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. 
# This function should return an updated dictionary.

# Example: delete_book(dictionary, “Mark Twain”)

def delete_book(dizionario:dict, author:str)-> dict:
    return dizionario, dizionario.pop(author)

print(delete_book({"key1":1,"key2":2,"key3":3}, "key1"))




# 3. Personal Info:

# Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. 
# Make occupation, location, and age optional parameters. Use this function to create profiles for different people, 
# demonstrating how it handles these optional parameters.

# Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)

def build_profile(name, surname, occupation = None, location = None, age= None):
    return name,surname,occupation,location,age

print(build_profile("Marco","Cirelli","Carrozziere","Texas",36))

def build_profile(name, surname, **args):
    return name,surname,args

print(build_profile("Marco","Cirelli",occupazione = "Carrozziere", città = "Texas",età = 36))

# 4. Event Organizer:

# Write a function called plan_event() that accepts an event name, a list of participants, and an hour. 
# The function should return a dictamionary that includes the event name and a list of the participants. 
# Call this function with varying numbers of participants to plan different events.

# Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

def plan_event(event_name:str, partecipants: list, hour:str) -> dict:
    nomeevento = event_name
    newdict = {nomeevento:[]}
    newdict[nomeevento] = partecipants
    return newdict
print(plan_event("Corso Cybersec", ["Pippo","Paperino", "Pluto","Gatto Silvestro", "Pippo Baudo"], "9am"))

# user_name = 'JohnDoe'
# user_info = {user_name: {'email': 'john@example.com', 'age': 30}}
# print(user_info)


# Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.

# Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)
def modify_event(diz:dict, eventname:str, lista2: list, orario:str):
    new_dict = {}
    for k,v in diz.items():
        if k == eventname:
            new_dict[eventname] = v + lista2
        else:
            print("No event with that name.")
    return new_dict



print(modify_event({'Corso Cybersec': ['Pippo', 'Paperino', 'Pluto', 'Gatto Silvestro', 'Pippo Baudo']}, "Corso Cybersec", ["Alice", "Bob", "Charlie"], "4pm"))

# 5. Shopping List:

# Write a function called create_shamopping_list() that accepts a store name and any number of items as arguments. 
# It should return a dictionary with the store name and a set of items to buy there. 
# Test the function with different stores and item lists.

# Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

# Write a function called print_shopping_list() that accepts a dictionary and a store name, 
# then prints each item from that store's shopping list.

# Example: print_shopping_list(dictionary, "Grocery Store")



def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for k,v in da_rimuovere.items():
        counter = 0
        lista_nuova= lista.copy()
        while v > counter:
            if k in lista:
                lista_nuova.remove(k)
                counter+=1
            else:
                break
        
       
    return lista_nuova


print(rimuovi_elementi([1,2,3,2,4,5], {2:2}))


# def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
#     superlista = []
#     dizionario_vuoto= {}
#     for i in voti:
#         for k,v in i.items():
#             if k not in dizionario_vuoto:
#                 dizionario_vuoto= {k[v]}
#             if k in dizionario_vuoto:
#                 dizionario_vuoto[k] = v
#         superlista.append(dizionario_vuoto)
#     return superlista

# print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
 
def aggregate_grades(grades_list):
    aggregated_grades = {}
    
    for grade_dict in grades_list:
        #codi facendo si sta estraendo il nome e il voto dello studente
        name = grade_dict['nome']
        grade = grade_dict['voto']
        print(grade,name)
        if name in aggregated_grades:
            aggregated_grades[name].append(grade)
        else:
            aggregated_grades[name] = [grade]
    
    return aggregated_grades

# Test the function
grades = [{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]
print(aggregate_grades(grades))


#print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
#{'Alice': [90, 85], 'Bob': [75]}

# def plan_event(event_name:str, partecipants: list, hour:str) -> dict:
#     nomeevento = event_name
#     newdict = {nomeevento:[]}
#     newdict[nomeevento] = partecipants
#     return newdict
d = {'k1': 1, 'k2': 2}

d['k3'] = 3
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

d['k1'] = 100
print(d)
# {'k1': 100, 'k2': 2, 'k3': 3}


# def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
#     dizionario_vuoto= {}
#     for i in voti:
#         for k,v in i.items():


#             # if k not in dizionario_vuoto:
#             #     lista = [v]
#             #     dizionario_vuoto[k] = lista
#             # else:
#             #     dizionario_vuoto[k] = lista.append(v)
        
#         return dizionario_vuoto
    

# def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
#     dizionario_vuoto= {}
#     for i in voti:
#         for k,v in i.items():


            # if k not in dizionario_vuoto:
            #     lista = [v]
            #     dizionario_vuoto[k] = lista
            # else:
            #     dizionario_vuoto[k] = lista.append(v)
        
        #return dizionario_vuoto
    
#print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca 
#un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
def filtra_e_mappa(dizionario: dict) -> dict:
    for k,v in dizionario.items():
        if v > 20:
            dizionario[k] = v - v * 10 / 100
        else:
            continue
       
    return dizionario

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
# For example:
# print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))

# print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))

	

# {'Zaino': 45.0, 'Quaderno': 19.8}

# print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 

# {}




# PARTE 1
# Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
# PARTE 2
# Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

# For example:
# Test 	Result

# contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
# print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
# print(update_contact(contact, "Mario Rossi", telefono=123456789))

	

# {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}
# {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}





























