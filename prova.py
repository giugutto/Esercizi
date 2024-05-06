def blackjack_hand_total(cards: list[int]) -> int:
    x = sum(cards)
    v = 11
    if x > 21:
        if v in cards:
            cards.remove(v)
            cards.append(1)
            return(sum(cards))
    else:
        return(x)

blackjack_hand_total([2,3,5])
blackjack_hand_total([5,5,11])
blackjack_hand_total([1,10,11])
blackjack_hand_total([1, 10, 11])	
blackjack_hand_total([1, 10, 5])
blackjack_hand_total([11, 5, 3])
################################################
def construct_rectangle(area: float) -> list[float]: # comes from input
    possibilities = [] # initialize a list
    for length in range (1, area+1): # go through every possible length
        width, invalid = divmod(area, length) # find the width and its validity
        if not invalid: # if there's no remainder
            possibilities.append((length, width)) # add this
    lista_temp:list = []
    for i in possibilities:
        b = list(i)
        if b[0] >= b[1]:
            lista_temp.append(b)
        else:
            continue
    #lista_temp_2: list = []
    temp_1: int = 100000000000000000000000000
    best_pair: list = None
    for x in lista_temp:
        a = x[0] - x[1]
        if temp_1 > a:
            temp_1 = a
            best_pair = x

    return best_pair



print(construct_rectangle(30))

##################################################################

#Scrivi una funzione che accetta una stringa come input,
#rimuove le parole non significative comuni stop_words e restituisce un dizionario in cui le chiavi sono parole
#univoche nel testo rimanente (ignorando la distinzione tra maiuscole e minuscole e la punteggiatura)
#e i valori sono le frequenze di quelle parole.

#For example: stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
#text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
#print(word_frequency(text, stopwords))

import string
def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    
    x = text.lower()
    punct = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for c in punct:
        x = x.replace(c, "")
    x = x.split()
    for i in x:
        if i in stopwords:
            x.remove(i)
        else:
            continue
    dictionary = {}
    for i in x:
        if i in dictionary.keys():
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    return dictionary

    
print(word_frequency("The quick brown fox jumps over the lazy dog. The dog is very lazy.",['the', 'and', 'is', 'in', 'on', 'of']))


# Hai il compito di indagare su un caso di numeri mancanti! Ti viene fornito un elenco di numeri univoci (nums) da 1 a n, 
# dove n è la lunghezza dell'elenco. 
# Sembra però che ci sia un problema: mancano alcuni numeri!
# La tua missione è scrivere una funzione che prenda come input questo elenco di numeri (nums) potenzialmente incompleti.
# Questo elenco rappresenta i numeri esistenti, ma alcuni numeri tra 1 e n potrebbero mancare.
# La funzione restituisce una nuova lista contenente tutti i numeri mancanti da 1 a n che non sono presenti nella lista originale. 



def find_disappeared_numbers(nums:list) -> list:
    x = min(nums)
    y = len(nums)
    missingn: list = []
    for i in range(x,y + 1):
        if i not in nums:
            missingn.append(i)
        else:
            continue
    return missingn


print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))







def is_subsequence(s: str,t: str):
    vuota = []
    for i in s:
        if i in t:
            vuota.append(i)
        else:
            continue
    a = "".join(i for i in vuota)
    if a == s:
        return True
    else:
        return False
print(is_subsequence("ask","ciask"))

# Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari.
# Restituisce l'elenco riorganizzato.
def even_odd_pattern(nums: list[int]) -> list[int]:
    list = []
    list_disp = []
    for i in nums:
        if i % 2 == 0:
            list.append(i)
        else:
            list_disp.append(i)
        
    list_fin = list + list_disp
    return list_fin
print(even_odd_pattern([3,4,6,7,1,12]))
        

#Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input

def prime_factors(n: int) -> list[int]:
    result = []
    i = 2

    while i<=n:
        if n%i==0:
            result.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        result.append(n)
    return result  
print(prime_factors(4))



# Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). 
# Questi gioielli hanno vari valori, alcuni più preziosi di altri. 
# Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.
# Qual è la svolta?
# Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). 
# A noi però interessano solo valori distinti, ovvero gioielli con valori unici.
# Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). 
# Se nello scrigno sono presenti almeno tre valori distinti, 
# la funzione dovrebbe restituire il valore del terzo gioiello distinto di maggior valore.
# Ma c'è un problema! 
# Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali),
# la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.

def third_max(nums: list[int]) -> int:
    resultantList = list(set(nums))
    if len(resultantList) == 2:
        return max(resultantList)
    elif len(resultantList) == 1:
        return resultantList[0]
    for i in range(3):
        if len(resultantList) == 1:
            continue
        resultantList.remove(max(resultantList))
        
    return max(resultantList)
        


print(third_max([3,2,1]))
print(third_max([1,2]))
print(third_max([2,2,3,1]))
print(third_max([2]))
print(third_max([2,2,3,2,2]))









    # first_max = second_max = third_max = float('-inf')
    # pass