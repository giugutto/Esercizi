#non ci posso essere spazi nella dichiariazione della variabile
#al posto degli spazi mettiamo un'underscore
#dopo i 2 punti c'è il typing e viene ignorata da python
#quindi se mettiamo un int e scriviamo un float, esso rimane un int
#quando darà un float come valore
nome_variabile_1: int = 17
nome_variabile: float = 17.0
nome_variabile: bool = True #(or False)
nome_variabile_1 += 6.7
print(nome_variabile_1) #come puoi vedere, il tipo di dato è un int

#da un float a un double, 
# cambia che con un float abbiamo a disposizione 32 bit,
# mentre per i double 64.


#aggiungiamo 5 alla nostra variabile.
#python sostituirà il valore aggiornato sulla stessa variabile.
nome_variabile_1 = nome_variabile_1 + 5

variabile_float: float = 5.0
variabile_float = 5.0 + 10.0 #float

variabile_int: int = 10
variabile_int = 10 + 5 #int

#il modo più veloce per aggiornare una variabile è:
nome_variabile += 5.5
#il più uguale è la stessa cosa di fare
nome_variabile = nome_variabile + 5.5

####string
nome_variabile_str: str = "ciao" #puoi anche mettere 1 apice, 
#ovvero 'ciao'

# troviamo il punto di mezzo di una lista
# se essa è dispari, abbiamo bisogno di una floor division

lunghezza_lista: int = 7

punto_di_mezzo: int = 7 // 2

#se volessimo arrotondare per eccesso, useremo il metodo round
import math
lunghezza_lista:int = 9
puntodimezzo: float = 9 / 2
print(math.ceil(puntodimezzo))

#per vedere tutte le funzioni di una libreria, possiamo sia 
# andare sulla documentazione ufficiale, oppure,
# scrivere nomedellalibreria. e si aprirà una finestrella 
# con le funzioni
#math.

#variabili booleani
variabile1: bool = True
variabile2: bool = False
#le operazioni che posso fare sono and, or, not

print(variabile1 and variabile2)
print(variabile1 or variabile2)
print(not variabile1)

#AND torna vero solo quando le 2 variabili sono true, in 
#questo caso torna false(è il prodotto di 2 variabili, 
#che ha come valori 0 o 1)
#OR torna vero se almeno 1 delle varibili è true
#(somma tra 2 variabili che hanno come valori 0 e 1)
#NOT torna false, perché è True, quindi nega il valore della 
#variabile corrente

#operatori condizionali
#come dichiarare un if
#alla fine una condizione deve avere un true o un false
#questo snip di codice non etrerà mai nella condizioni,
#perché variabile1 AND variabile2 è uguale a false

if variabile1 and variabile2:
    print(f"{variabile1 and variabile2}")

#mentre variabile1 OR variabile 2 è false

if variabile1 or variabile2:
    print(f"{variabile1 and variabile2}")

#OR
# a: bool 
# b: bool
# come faccio a sapere il risultato di a or b?
# calcoliamoli
#sommiamoli
# a   b   or
# 0   0    0 
# 0   1    1
# 1   0    1
# 1   1    2 aka 1

# AND
# moltiplichiamoli
# a    b   and
# 0    0   0
# 0    1   0
# 1    0   0
# 0    1   1

# quella piu esterna scriveremo 01 01 
# mentre quella più interna 00 11

x:int = 10

if x > 0 and x < 20:

    print(f"{variabile1 and variabile2}")
#lo stampa? sì!


a: bool = True
b: bool = True
if a and b:
    print(f"Sono nel primo")

elif a or b:
    print(f"Sono nel secondo")

else:
    print(f"Sono nell'else")
# potremmo anche scrivere
# elif not(a and b)
#se mettiamo un if dopo un if,entrambe le condizioni verranno valutate!!!
#mentre se mettiamo un if e poi un elif, elif NON verrà verificato

#coem fare lo swap?

lista: list = [1,2,3,4,5]

for i in range(len(lista) -1):

    if lista[i] > lista[i+1]:

        temp: int = lista[i]

        lista[i] = lista[i+1]

        lista[i+1] = temp

#stesso esempio dei secchi e la sabbia
#elif è un modo di fare condizioni alternative
#se si entra nell'if, elif e else NON vengono eseguiti
#se if è falso va nell'altro if elif or else
# else viene eseguito solo quando tutto quello prima 
# è falso


##formatter
#vogliamo sapere il valore di x?
#all'interno delle parentesi graffe troviamo la variabile di x
#quindi stamperà il suo valore
# print(f"x:{x}")
# for x in range(10):
#     print(f"x:{x}")


#CICLI
#esistono 2 tipi di cicli for and while
#i cicli servono per scorrere le collection
#liste
#dizionario
#posizioni     0 1 2 3 4
lista: list = [1,2,3,4,5]
#CICLO FOR
for numero in lista:
    print(f"x^2: {numero**2}")
# entrambe stampano la stessa cosa, ma con il seguente modo
# prenderemo gli indici
#range prende da 0 al numero che gli diciamo -1, in questo caso alla
#lunghezza della lista, in questo caso da 0 a 4
for numero in range(len(lista)):
                 #lista in posizione 1, perché numero vale 0
                 #e il valore dell'indice 0 è 1   
    print(f"x^2: {lista[numero] ** 2}")


#CICLO WHILE
#ciclo while serve per ripetere infinitamente un bocco di codice
#scriviamo la stessa cosa del ciclo for con il ciclo while
contatore: int = 0
while contatore < len(lista):
    print(f"x^2: {lista[contatore]**2}")
    contatore +=1

#dizionari
anagrafe: dict = {
    "persona1":"Flavio",
    "persona2":"Marco",
    "persona3":"Leonardo",
}

#come accediamo al valore della chiave?
anagrafe["persona1"]
#se proviamo ad accedere a un valore che non esiste ci darà un 
#keyerror
#come aggiungiamo una nuova chiave valore su python?
anagrafe["persona4"] = "Bardh"
#per aggiornare il valore di una chiave andremo a fare cosi
anagrafe["persona2"] = "Bardh"

#aggiungiamo il valore della chiave se la chiave non esiste altrimenti lo stampiamo
key:str = "persona100"

if key in anagrafe:
    print(anagrafe[key])
else:
    anagrafe[key] = None

voti: list = [{"nome" : "Flavio", "voto":18}, {"nome" : "Flavio", "voto":25}, {"nome" : "Marco", "voto":25}]

aggr: dict = {}

for i in voti:
    nome = i["nome"] #STIAMO ESTRAENDO I VALORI DELLE CHIAVI
    voto = i["voto"]

    if nome in aggr:
        aggr[nome].append(voto)
    else:
        aggr[nome] = [voto]

#come esploriamo i dizionari con un ciclo for?

for key, value in aggr.items():
    print(key,value)
#se usiamo questa funzione, stamperemo tutti i valori senza le chiavi
for value in aggr.values():
    print(value)

#mentre se usiamo questa funzione ci stampa solo le chiavi
for ket in aggr.keys():
    print(key)


#i diozionari possono essere annidati quindi posso dichiarare un 
#dizionario che ha delle chiavi e come valori ha un dizionario
aggr: dict = {
    "key1": {
        "key_1_1": {
            "floor":"0"

        }
    }
}
#accediamo al valore più interno
x = aggr["key1"]["key_1_1"]["floor"]

print(x)

# formatting
# /n a capo
# /t Tab
# \' costringe a mettere un apice all'interno della stringa
# \\ il primo slash forza il secondo ad essere interpretato come carattere

#LISTE,DIZIONARI E SET SONO MODIFICABILI, MENTRE LE TUPLE NO
#SUL SET NON CI SONO DULICATI

def get_numbers():
    a=1
    b= 2
    return a, b

t = get_numbers()
a,b = get_numbers()
print(t,a,b)


def print_somma(a:int, b:int):
    somma = a+ b 
    print(somma)

print_somma(10,20)


# Write a function to find all numbers divisible by 7, 
# not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers should be stored in a list and returned as output.

def find_numbers(num1,num2):
    listan = []
    for i in range(num1,num2 + 1):
        if i % 7 == 0:
            listan.append(i)
    
    for x in listan:
            if x % 5 == 0:
                listan.remove(x)
    return listan

find_numbers(2000, 3200)



# Write a function to calculate the factorial of a number given as input. 
# The number should be returned as output. For example:

#     Input: 8
#     Output: 40320

def factorial_numer(num1):
    x = num1
    for i in range(1, num1):
        x *= i

    print(x) 
    
factorial_numer(8)
1,2,3,4,5,6,7,8


# Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers. 
# The list is given as input to the function. All factorials should be returned as output. 
# For example:

# Input: [2, 5, 8, 10]
# Output: [2, 120, 40320, 3628800]

def fun_4(num1,num2,num3,num4):
    x = num1
    for i in range(1, num1):
        x *= i

    print(x) 
    v = num2
    for i in range(1, num2):
        v *= i

    print(v) 
    a = num3
    for i in range(1, num3):
        a *= i

    print(a) 
    b = num4
    for i in range(1, num4):
        b *= i

    print(b) 

fun_4(2,5,8,10)

# Given an integer n as input, 
# write a function to generate a dictionary that contains (i, i*i) 
# as (key, value) pairs such that i is an integer between 1 and n (both included). 
# The function should return the dictionary as output. For example:

#     Input: 8
#     Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def potenza(n):
    dizionariovuoto = {}
    for i in range(1, n +1):
        x = i ** 2
        dizionariovuoto[i] = x
    return dizionariovuoto
print(potenza(8))

# Write a function that accepts a string with a comma-separated sequence of words as input 
# and prints the words as a comma-separated sequence after sorting them alphabetically.
# For example:

# Input: without,hello,bag,world
# Output: bag,hello,without,world

def ordina(string:str) -> str:
    x = string.split(",")
    x.sort()
    x = ",".join(x)
        
    return x
print(ordina("without,hello,bag,world"))

# def ordina(string:str):
#     listav = []
#     stringa = ""
#     x = string.split(",")
#     for i in x:
#         listav.append(i)
#     listav.sort()
#     for i in listav:
#         stringa += i
#         #lista.index(i) torna la posizione
        
#     return stringa


# Write a function that accepts a list of sentences 
# (string) as input and returns each line as output 
# after capitalising all sentence characters. For example:

#     Input: Practice makes perfect
#     Output: PRACTICE MAKES PERFECT
def senteces(stringa:str):
    x = stringa.upper()
    return x
    
print(senteces("Practice makes perfect"))