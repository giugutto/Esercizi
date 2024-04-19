# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

# pizze: list = ["Boscaiola", "Crostino", "Wrustel e patatine"]

# for i in pizze:
#     print("Mi piace la", i)

# print("Mi piace tantissimo la pizza!")

# # 4-2. Animals: Think of at least three different animals that have a common characteristic. 
# # Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# # • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# # • Add a line at the end of your program, stating what these animals have in common. 
# # You could print a sentence, such as Any of these animals would make a great pet!

# animals: list = ["Dog","Cat","Elephant"]

# for animal in animals:
#     print(animal)
# print("These animal have 4")

# #4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

# for i in range(1,21):
#     print(i)

# # 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
# # (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

# number = []
# for i in range (1, 1000000):
#     print(i)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers.

# numbers: list = [i for i in range(1, (10**6)+1)]
# print(numbers)
#print(min(numbers), max(numbers), sum(numbers))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
# Use a for loop to print each number.

# for i in range(1, 20, 3):
#     print(i)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
# Use a for loop to print the numbers in your list.

# multipli: list= [i for i in range(3,31) if i%3==0]
# for i in multipli:
#     print(i)

# 4-8. Cubes: A number raised to the third power is called a cube. 
# For example, the cube of 2 is written as 2**3 in Python. 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubes = []
for i in range(1,11):
    cubes.append(i**3)
print(cubes)


#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubi: list = [i**3 for i in range(1,11)]
print(*cubi)

#  4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#  • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#  • Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#  • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

cubes = []
for i in range(1,11):
    cubes.append(i**3)
print(cubes)
print("I primi numeri della lista sono", cubes[0:3])
print("I in mezzo alla lista sono", cubes[3:7])
print("Gli ultimi numeri della lista sono", cubes[7:11])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
#  Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#  • Add a new pizza to the original list.
#  • Add a different pizza to the list friend_pizzas.
#  • Prove that you have two separate lists. 
#  Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
#  Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
#  Make sure each new pizza is stored in the appropriate list.

pizza: list = ["Boscaiola", "Crostino", "Wrustel e patatine","Margherita"]

friend_pizze: list = ["Boscaiola", "Crostino", "Wrustel e patatine","Salsiccia e rucola"]

for i in pizza:
    print(f"My favourite pizzas are: {i}")

for i in friend_pizze:
    print(f"My favourite pizzas are: {i}")

# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.
pass

# 4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. 
# You won’t use much of it now, but it might be interesting to skim through it.