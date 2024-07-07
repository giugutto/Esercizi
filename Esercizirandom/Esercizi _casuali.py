#Creare una tupla contenente il quadrato dei numeri interi da 1 a 5.
quadrato_tuple: tuple = tuple(i ** 2 for i in range(1, 6))
print(quadrato_tuple)
#Creare una tupla con i seguenti elementi: "mela", "banana", "kiwi".
tup = ("mela","banana","kiwi")

print(tup[1])
#Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.

varcon = 0
for i in tup:
    if i == "mela":
        varcon += 1
    else:
        continue

print(varcon)
#Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga.
def lunga(lista)-> list:
    parola = ""
    for i in lista:
        if len(i) > len(parola):
            parola = i
        else:
            continue
    return parola

print(lunga(["ciao","mamma","prova","gallo","galline","patata"]))


#Given a list of numbers, write a program to: Swap the first and last elements of the list and print the modified list.
numbers = [1, 2, 3, 4, 5]
secchiello1 = ""
secchiello2 = ""
secchiello1 = numbers[0]
secchiello2 = numbers[4]
numbers[0] = secchiello2
numbers[4] = secchiello1
print(numbers)


# Exercise 10: Finding Maximum and Minimum by Index
# Given a list of integers, write a program to:

# Find and print the index of the maximum value.
# Find and print the index of the minimum value.

numbers = [34, 12, 56, 78, 23, 89, 3, 45]
massimo = 1
minimo = 100
for i in numbers:
    if i > massimo:
        massimo = i
    else:
        continue
for i in numbers:
    if i < minimo:
        minimo = i
    else:
        continue
print(f"Il valore massimo è {massimo}, il valore minimo è {minimo}")



rows = 5
k = 2 * rows -2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end='')
    #k = k + 1
    for j in range(0, i + 1):
        print('*', end='')
    print("")