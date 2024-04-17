#Giuseppe Guttoriello
#17/07/24

#print("Hello World!")

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name: str = "Gabriele"

message: str = f"Hello {name}, would you like to drink something today?"

print(message)

#2-4. Name Cases:
#Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name: str = "Giuseppe"

low: str = name.lower()
up: str = name.upper()
cap: str = name.capitalize()

superstringa = (f"Il nome in lettere minuscole è {low}, quello a lettere maiuscole è {up} e infine con la prima lettera maiuscola è {cap}")

print(superstringa)

#2-5. Famous Quote: Find a quote from a famous person you admire.
#Print the quote and the name of its author. Your output should look something like the following, 
#including the quotation marks: Albert Einstein once said, 
#“A person who never made a mistake never tried anything new.”

name: str = "Elliot Alderson"
quote: str = "\"Hackers...they never trust each other\""

stringafinale: str = (f"{name} in one of the episode said {quote}")

print(stringafinale)


# 2-6. Famous Quote 2: Repeat Exercise 2-5,
# but this time, represent the famous person’s name using a variable called famous_person. 
# Then compose your message and represent it with a new variable called message.
#  Print your message.



famous_person = name

message: str = (f"{famous_person} in one of the episode said {quote}")

print(message)

