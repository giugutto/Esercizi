# # 8-1. Message: Write a function called display_message()
# #that prints one sentence telling everyone what you are learning about in this chapter.
# # Call the function, and make sure the message displays correctly.

def message() -> str:
    messaggio = "Hi everyone, i'm learning function in python"
    return messaggio

print(message())

# # 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title.
# # The function should print a message, such as "One of my favorite books is Alice in Wonderland".
# # Call the function, making sure to include a book title as an argument in the function call.

def favourite_book(title:str):
    x = print(f"One of my favourite books is {title}")
    return x

favourite_book("Il profumo")

# # 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message
# # that should be printed on the shirt.
# # The function should print a sentence summarizing the size of the shirt and the message printed on it.
# # Call the function once using positional arguments to make a shirt.
# # Call the function a second time using keyword arguments.

def make_shirt(size:str, text: str):
    x = print(size + text)
    return x

taglia = "S"
messaggio = " Stan"

make_shirt(taglia,messaggio)

make_shirt("XL", " ciao")

# # 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# # Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size: str = "L", messaggio: str = "I love python") -> str:
    return  size + ', ' + messaggio

print(make_shirt())

print(make_shirt(size="L"))

print(make_shirt(size = "XL", messaggio = "Port scanning is not a crime!"))

# # 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country.
# # The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
# # Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city: str , country: str) -> str:
    return(f"{city} is in {country}")

print(describe_city(city="Rome", country="Italy"))
print(describe_city(city="Bologna", country="Italy"))
print(describe_city(city="Parigi", country="France"))

# # 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
# # The function should return a string formatted like this: "Santiago, Chile".
# # Call your function with at least three city-country pairs, and print the values that are returned.


def city_country(city: str, country: str) -> str:
    return (f"{city}, {country}")

print(city_country("Barcellona", "Spain"))
print(city_country("Amburgo", "Germany"))
print(city_country("Bologna", "Italy"))

# # 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
# # The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
# # Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly.
# # Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
# # If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
# # Make at least one new function call that includes the number of songs on an album.

def make_album(artist:str , title:str, song_number: int = None) -> str:
    if song_number != None:
        return {artist:[title, song_number]}
    return{artist,title}

print(make_album("Nirvana","Nevermind"))
print(make_album("Metallica","Master of Puppets", 10))
print(make_album("Lil Peep","Crybaby"))

# 8-8. User Albums: Start with your program from Exercise 8-7.
# Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
# Be sure to include a quit value in the while loop.

def make_album(artist:str = None , title:str = None , song_number: int = None) -> str:
    while artist==None or title == None or song_number== None:
        artist = input("Insert the artist")
        title = input("Insert a title")
        song_number = input("Insert the number of the song in the Album")
    if song_number != None:
        return {artist:[title, song_number]}
    

print(make_album())

# 8-9. Messages: Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message.

messages: list = ["Angelo mangia le ostriche", "Gino beve dello champagne", "Manuel si lava il viso"]

def mess(messages):
    for i in messages:
        print(i)

mess(messages)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages()
# that prints each text message and moves each message to a new list called sent_messages as it’s printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.


messages = ["I love encoding", "Obfuscate me", "verba volant, scripta manent"]
def send_messages(messages):
    sent_messages=[]
    while messages!=[]:
        sent_messages.append(messages[0])
        messages.pop(0)
    else:
        return sent_messages

sent_messages=send_messages(messages)
print(messages, sent_messages)

# 8-11. Archived Messages: Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.

messages = ["I love encoding", "Obfuscate me", "verba volant scripta manent"]
sent_messages=send_messages(messages[:])
print(messages,sent_messages)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwich that’s being ordered.
# Call the function three times, using a different number of arguments each time.

def sandwich(item:list):
    for i in item:
        print(i)

sandwich(["pomodori","formaggio","cetrioli"])
sandwich(["tonno","pomodori","maionese"])
sandwich(["carciofini","tonno","panna","cervello di bue"])


# 8-13. User Profile:  Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you.
# All the values must be passed to the function as parameters.
# The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

def build_profiles(first_name:str, last_name:str, **kvarg):
    mess = (f"{first_name} {last_name}")
    if kvarg:
        for i in kvarg.items():
            mess += (f", {i[0]} {i[1]}")

    return mess

print(f"{build_profiles('Giuseppe','Guttoriello', age = 27,hair = 'brown', eyes = 'brown')}, {build_profiles('Marco','Fintisi', age = 22,hair = 'blonde', eyes = 'blue')}")

# 8-14. Cars: Write a function that stores information about a car in a dictionary.
#The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
# Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly.

def car(manufacter:str , model:str, **kwargs:str) -> str:
    always = (f"{manufacter} {model}")
    if kwargs:
        for i in kwargs.items():
            always += (f" {i[0]} {i[1]}")
    return always

print(f"{car('Alfaromeo','Giulietta', color='red')}")

# # 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py.
# # Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

import funcar as c

x = c.car('Lamborghini','RGT', color = "black")

print(x)

# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file.
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import funcar

print(funcar.car('Lamborghini','RGT', color = "black"))
from funcar import car
print(car('Lamborghini','RGT', color = "black"))
from funcar import car as c
print(c('Lamborghini','RGT', color = "black"))
from funcar import *
print(funcar.car('Lamborghini','RGT', color = "black"))



# Create a function that takes a student's name and their scores in different subjects as input.
# The function calculates the average score and prints
# the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
# Create a for loop to iterate over a list of students and scores, calling the function for each student.


def average(name: str, sub_1: int, sub_2:int, sub_3) -> str:
	if (sub_1 + sub_2 + sub_3) / 3 > 60:
		return(f"{name} " + str((sub_1 + sub_2 + sub_3) / 3)) + (" You passed the exam ")
	else:
		return(f"{name}" + str((sub_1 + sub_2 + sub_3) / 3)) + (" I'm sorry, you didn't pass the exam")
print(average("Giuseppe",100,92,94))


students_list: list = ['Marco','Giulia','Francesca']
grades_list: list = [[81,45,92,56],[78,67,100,70],[91,71,66,80]]

def average_(num: list):
    scores_sum = sum(num)
    scores_average = scores_sum / len(num)
    return scores_average

def check_student(student: str,scores: list):

    average: float = average_(scores)
    if average >= 60:
        print(f"{student}, {average}. You passed the exam.")
    else:
        print(f"{student}, {average}. I'm sorry, you didn't pass the exam.")

for i in range(len(students_list)):
    check_student(students_list[i],grades_list[i])

# # 2. Guess the Number Game:

# # Create a function that generates a random number within a range specified by the user.
# # Prompt the user to guess the number within a specified maximum number of attempts.
# # Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
# # Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
import random

def process_input():
    num_1 = input("Please enter a number: ")
    num_2 = input("please insert your last number")
    num_1_int = int(num_1)
    num_2_int = int(num_2)
    x = random.randint(num_1_int,num_2_int)
    for i in range(5, 0, -1):
        a = input(f"Guess the number! You've {i} attempts!")
        numberint = int(a)
        if numberint > x:
            print(f"Too high")
        elif numberint < x:
            print(f"Too low!")
        elif numberint == x:
            print("Congrats, you guessed the number!")
            break



process_input()


# Create a function that defines a product with a name, price, and quantity.
# Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
# The function should calculate the cart total and apply any discounts or taxes.
# Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.


def product(name, price, quantity):
    return name, price, quantity

def product_viewer(product, taxes, discount=0):
    name, price, quantity = product
    discount=(discount*price)/100 if discount else 0
    taxes=(taxes*(price-discount))/100
    print("Viewing item:" + name) 
    print("Price:" +  price) 
    print("Price after discount:" + (price-discount))
    print("Price after taxes:" + (price+taxes)) 
    print("Quantity:" + quantity) 
    print("Total price before taxes:" (price-discount)*quantity) 
    print("Total price after taxes:" + (price-discount+taxes)*quantity)
          

def cart(taxes, discount, *args, add = None, remove=None,view=None):
    carrello = [*args]
    if add:
        carrello.append(add)
        print(carrello)
    if remove:
        carrello.remove(remove)
        print(carrello)
    if view in carrello:
        product_viewer(view,taxes,discount)
    for i in carrello:
        product_viewer(i, taxes,discount)




cart(0,11,product('Leonardo', 100, 2), product('Cccio', 100, 1), add=product('gianni', 45, 1))



# Create a function that reads a text file and counts the number of occurrences of each word.
# The function should print a report showing the most frequent words and their number of occurrences.
# You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
# Implement error handling to handle missing files or other input issues.


def reads(file):
    listaparole = []
    listaparole_1 = []
    with open(file, 'r') as f:
        x = f.readlines()
        for i in x[1].split():
            listaparole.append(i)
    with open(file, 'r') as f:
        x = f.readlines()
        for line in x:
            for word in line.split():
                listaparole_1.append(word)
    def count_occurrences(list1, list2):
        occurrences = {}
        for word in list1:
            occurrences[word] = list2.count(word)
        return occurrences
          
    print(count_occurrences(listaparole, listaparole_1))
    x = count_occurrences(listaparole, listaparole_1)
    
    max_key = max(x, key=x.get)
    
    print("The word most repeated in the text is", max_key, "and it's repeated", x[max_key],"time")
reads('file.txt.txt')














########################################################################################################
#questa funzione implementa il bubble sort
# a: list = [6, 1, 8, 3, 5, 7, 2, 4]

# for x in range(len(a)):
#     for y in range(len(a) - 1):
#         if(a[y] > a[y+1]):
#            # swap[a[y], a[y+1]]
#             temp = a[y]
#             a[y] = a[y + 1]
#             a[y + 1] = temp

# print(a)

# import time
# a: list = [i for i in range(1, 10*5)]

# def bubble_sort(a):
#     start: float = time.time()
#     for x in range(len(a)):
#         swap_flag = False
#         for y in range(len(a) - x -1):
#             if(a[y] > a[y+1]):
#                 swap_flag = True
#                 # swap[a[y], a[y+1]]
#                 temp = a[y]
#                 a[y] = a[y + 1]
#                 a[y + 1] = temp

#         if swap_flag is False:
#             return a, time.time() - start
#     return a, time.time() - start

# print(bubble_sort(a))

