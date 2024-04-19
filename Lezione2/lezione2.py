# #Giuseppe Guttoriello
# #17/07/24

# #print("Hello World!")

# #2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
# #Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

# name: str = "Gabriele"

# message: str = f"Hello {name}, would you like to drink something today?"

# print(message)

# #2-4. Name Cases:
# #Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

# name: str = "giuseppe"

# low: str = name.lower()
# up: str = name.upper()
# cap: str = name.capitalize()

# superstringa = (f"Il nome in lettere minuscole è {low}, quello a lettere maiuscole è {up} e infine con la prima lettera maiuscola è {cap}")

# print(superstringa)

# #2-5. Famous Quote: Find a quote from a famous person you admire.
# #Print the quote and the name of its author. Your output should look something like the following, 
# #including the quotation marks: Albert Einstein once said, 
# #“A person who never made a mistake never tried anything new.”

# name: str = "Elliot Alderson"
# quote: str = "\"Hackers...they never trust each other\""

# stringafinale: str = (f"{name} in one of the episode said {quote}")

# print(stringafinale)


# # 2-6. Famous Quote 2: Repeat Exercise 2-5,
# # but this time, represent the famous person’s name using a variable called famous_person. 
# # Then compose your message and represent it with a new variable called message.
# #  Print your message.



# famous_person = name

# message: str = (f"{famous_person} in one of the episode said {quote}")

# print(message)

# #2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
# #Assign the value 'python_notes.txt' to a variable called filename. 
# #Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

# filename: str = "python_notes.txt"

# print(filename.removesuffix(".txt"))

# #3-1. Names: Store the names of a few of your friends in a list called names. 
# #Print each person’s name by accessing each element in the list, one at a time.

# names: list = ["Federico", "Marco", "Paolo", "Giovanni"]

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])


# # 3-2. Greetings: Start with the list you used in Exercise 3-1, 
# # but instead of just printing each person’s name, print a message to them. 
# # The text of each message should be the same, but each message should be personalized with the person’s name.

# print("Ciao", names[0], "Come stai?")
# print("Ciao", names[1], "Come stai?")
# print("Ciao", names[2], "Come stai?")
# print("Ciao", names[3], "Come stai?")


# #3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
# #Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

# mezzi: list = ["moto","macchina","aereo","nave"]

# print("Mi piacerebbe farmi un giro con la", mezzi[0])
# print("Di solito, mi muovo con la", mezzi[1])
# print("Sono andato in", mezzi[2], "poche volte")
# print("Non sono mai stato in una", mezzi[3])

# # 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
# # Make a list that includes at least three people you’d like to invite to dinner. 
# # Then use your list to print a message to each person, inviting them to dinner.

# nomi: list = ["Francesca", "Gabriele", "Arianna"]

# print("Hey ciao", nomi[0], "mi piacerebbe fare una cena per rivederci insieme a Gabriele e Arianna, che ne dici? fammi sapere")
# print("Eo", nomi[1], "sto organizzando una cena con Gabriele e Arianna, che ne dici se ci organizzassimo? Famme sape")
# print("Oi ciao", nomi[2], "! Io, Gabriele e Francesca stiamo organizzando una cena per rivederci, che ne dici di unirti a noi? fammi sapere :)")

# # 3-5. Changing Guest List: 
# #You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# #You’ll have to think of someone else to invite.
# # • Start with your program from Exercise 3-4. 
# #Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# # • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# # • Print a second set of invitation messages, one for each person who is still in your list.

# nomi: list = ["Francesca", "Gabriele", "Arianna"]

# print("Hey ciao", nomi[0], "mi piacerebbe fare una cena per rivederci insieme a Gabriele e Arianna, che ne dici? fammi sapere")
# print("Eo", nomi[1], "sto organizzando una cena con Gabriele e Arianna, che ne dici se ci organizzassimo? Famme sape")
# print("Oi ciao", nomi[2], "! Io, Gabriele e Francesca stiamo organizzando una cena per rivederci, che ne dici di unirti a noi? fammi sapere :)")
# print(nomi[1], "Non riesce a venire alla cena")
# nomi[1] = "Barbara"

# print(f"Ciao {nomi[0]}, sto organizzando una cena, ti va di venire? fammi sapere!")
# print(f"Ciao {nomi[1]}, sto organizzando una cena, ti va di venire? fammi sapere!")
# print(f"Ciao {nomi[2]}, sto organizzando una cena, ti va di venire? fammi sapere!")

# # 3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
# #Think of three more guests to invite to dinner.
# # • Start with your program from Exercise 3-4 or 3-5. 
# #Add a print() call to the end of your program, informing people that you found a bigger table.
# # • Use insert() to add one new guest to the beginning of your list.
# # • Use insert() to add one new guest to the middle of your list.
# # • Use append() to add one new guest to the end of your list.
# # • Print a new set of invitation messages, one for each person in your list.

# print(f"Ciao {nomi[0]},{nomi[1]},{nomi[2]}, ho scoperto che ci sono più posti disponibili, inviterò anche altre persone!")
# nomi.insert(0, "Marco")
# nomi.insert(1, "Angelo")
# nomi.append("Valerio")
# print(f"Ciao {nomi[0]}, sto organizzando una cena, ti va di venire? fammi sapere!")
# print(f"Ciao {nomi[1]}, sto organizzando una cena, ti va di venire? fammi sapere!")
# print(f"Ciao {nomi[2]}, sto organizzando una cena, ti va di venire? fammi sapere!")
# print(f"Ciao {nomi[3]}, sto organizzando una cena, ti va di venire? fammi sapere!")
# print(f"Ciao {nomi[4]}, sto organizzando una cena, ti va di venire? fammi sapere!")


# # 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# # • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# # • Use pop() to remove guests from your list one at a time until only two names remain in your list.
# # Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# # • Print a message to each of the two people still on your list, letting them know they’re still invited.
# # • Use del to remove the last two names from your list, so you have an empty list. 
# # Print your list to make sure you actually have an empty list at the end of your program.
# print("Posso invitare solo 2 persone per cena")
# nomi.pop(5)
# print(f"Hey ciao Arianna, purtroppo non posso più invitarti per cena, mi dispiace")
# nomi.pop(4)
# print(f"Hey ciao Barbara, purtroppo non posso più invitarti per cena, mi dispiace")
# nomi.pop(3)
# print(f"Hey ciao Francesca, purtroppo non posso più invitarti per cena, mi dispiace")
# nomi.pop(2)
# print(f"Hey ciao Valerio, purtroppo non posso più invitarti per cena, mi dispiace")
# print(f"Ciao {nomi[0]}, ti ricordo che sei ancora invitato a cena!")
# print(f"Ciao {nomi[1]}, ti ricordo che sei ancora invitato a cena!")
# del(nomi[0])
# del(nomi[0])
# print(nomi)


# # 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# # • Store the locations in a list. Make sure the list is not in alphabetical order.
# # • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# # • Use sorted() to print your list in alphabetical order without modifying the actual list.
# # • Show that your list is still in its original order by printing it.
# # • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# # • Show that your list is still in its original order by printing it again.
# # • Use ()  to change the order of your list. Print the list to show that its order has changed.
# # • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# # • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# # • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# # Print the list to show that its order has changed.


# places: list = ["Parigi","Londra","Amsterdam","Vienna","Barcellona"]

# print(sorted(places))
# print(places)

# print(sorted(places)[::-1])

# print(places)
# places.reverse()
# print(places)
# places.reverse()
# print(places)
# places.sort()
# print(places)
# places.sort(reverse=True)
# print(places)

# # 3-9. Dinner Guests: Working with one of the programs from Exercises 3,
# # use len() to print a message indicating the number of people you’re inviting to dinner.

# print(len(places))

# 3-10. Every Function: Think of things you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.


# things: str = ["Mouse", "Computer", "Keyboard", "Webcam", "Hard-disk"]

# things.insert(3, "Bottle")
# things.append("Screen")
# things.remove("Keyboard")
# things.pop(0)
# print(things)

# sorted(things)
# print(things)

# things.reverse()
# print(things)
# things.sort()
# print(things)
# things.sort(reverse=True)
# print(things)

# # 6-1. Person: Use a dictionary to store information about a person you know. 
# # Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. 
# # Print each piece of information stored in your dictionary.

# valori: dict = {"first_name":"Giuseppe", "last_name":"Guttoriello", "age":"27", "city":"Rome"}

# print(valori["first_name"])
# print(valori["last_name"])
# print(valori["age"])
# print(valori["city"])

# # 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# # Think of five names, and use them as keys in your dictionary.
# # Think of a favorite number for each person, and store each as a value in your dictionary.
# #  Print each person’s name and their favorite number
# # For even more fun, poll a few friends and get some actual data for your program.

nomi: dict = {"Alessio":"18", "Marta":"25", "Barbara":"93", "Valeria":"82", "Marco":"37"}

for i in nomi.items():
    print(f"{i[0]},{i[1]}")

# # 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# # • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# # • Print each word and its meaning as neatly formatted output. 
# # You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
# # Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

# glossary: dict ={
#     "variabile":"nome con un valore",
#     "reverse_shell":"personà si connetterà a noi e otteremo un terminale",
#     "cpu":"central process unit",
#     "ram":"random access memory",
#     "bind_shell":"noi ci connettiamo a qualcuno e otteremo un terminale"
#     }

# for i in glossary.items():
#     print(f"{i[0]}:\n{i[1]}")


# # 6-7. People: Start with the program you wrote for Exercise 6-1.
# #  Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
# #  Loop through your list of people. As you loop through the list, print everything you know about each person.


# valori: dict = {"first_name":"Giuseppe", "last_name":"Guttoriello", "age":"27", "city":"Rome"}

# valori1: dict = {"first_name":"Pippo", "last_name":"Franco", "age":"67", "city":"Bologna"}

# valori2: dict = {"first_name":"Angelo", "last_name":"Locarini", "age":"19", "city":"Sezze"}

# people: list = [valori, valori1, valori2]

# for person in people:
#     for item in person.items():
#         print(f"{item[0]},{item[1]}")

# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet. 

# pet_1: dict = {"species":"dog", "owner":"pippo"}
# pet_2: dict = {"species":"cat", "owner":"paperino"}
# pet_3: dict = {"species":"pig", "owner":"topolino"}

# animal: list = [pet_1, pet_2, pet_3]

# for animals in animal:
#     for item in animals.items():
#         print(f"{item[0]}",{item[1]})

# 6-9. Favorite Places: Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
# Loop through the dictionary, and print each person’s name and their favorite places.


# favourite_places: dict = {
#     "Luca": ["Marsiglia","Nantes","Lione"],
#       "Leonardo":["Siviglia","Valencia","Toledo"],
#         "Alessio":["Zurigo","Montreux","Lucerna"]
# }

# for i in favourite_places.items():
#     print(f"{i[0]},{i[1]}")


# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

nomi: dict = {"Alessio":["18", "83","62"],
               "Marta":["234", "8673","3242"],
                 "Barbara":["354", "675","54674"],
                   "Valeria":["754", "23423","685"],
                     "Marco":["4573", "2346","8563"]
                     }

for i in nomi.items():
    print(f"{i[0]},{i[1]}")


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, its approximate population,
# and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

cities: dict = {"Bologna":{"Country":"Italy", "Population":"389.200","Facts":"Is a country full of students"},
                 "Napoli":{"Country":"Italy","Population":"917.510","Facts":"City well know globally for the pizza"},
                 "Sicilia":{"Country":"Italy","Population":"4.814.016","Facts":"The city has some delicious sweets, like cannoli siciliani"}
                }

for i in cities.items():
    print(f"{i[0]},{i[1]}")    
                