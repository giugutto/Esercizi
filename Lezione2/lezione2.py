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