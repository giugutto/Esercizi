

# string = "ciao come va?"
# find = 'c'
# replace = 'b'

# result = ''


# for i in string:
#     if i == find:
#         result += replace
#     else:
#         result += i

# print(string)

# for i in range(len(string)):
#     if string[i] == find:
#         string[i] = replace
# print(string)

# abc
# def
# def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
#     alfabeto_1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     frase = ''
#     if offset % 24 == 0:
#         numero = offset // 24

#     for i in string:
#         if i == " ":
#             frase += " "
#             continue
#         x = alfabeto_1.index(i)
#         y = x + offset 
#         frase += alfabeto_1[y]

#     return frase

# print(caesar_cypher("prova ciao come va tutto ok",2))
# stringa = 'abcdefghijklmnopqrstuvwxyz'

#  for i in stringa:
# #     print(ord(i))

# # print(chr(117))
import random

def tartaruga_move(weather) -> int:
    x = random.randint(1, 10)
    passoveloce = 3
    passolento = -6
    scivolata = 1      
    if weather == "Pioggia" and x <=5:
        return passoveloce - 1
    if weather == "Pioggia" and x <=7:
        return scivolata - 1
    if weather == "Pioggia" and x <=10:
        return passolento - 1
    if x <= 5:
        return passoveloce
    elif x <= 7:
        return scivolata
    else:
        return passolento
    
print(tartaruga_move("Pioggia"))