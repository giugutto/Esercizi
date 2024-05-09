# Immaginiamo di avere un tipo speciale di sistema numerico in cui gli unici elementi costitutivi sono i numeri 2, 3 e 5. 
# Chiamiamo questi elementi costitutivi "fattori primi" perché non possono essere ulteriormente scomposti. 
# Un "numero brutto" in questo sistema è un numero costruito utilizzando solo questi fattori primi (2, 3 o 5). 
# Ad esempio, 6 (che può essere costruito come 2 x 3) è un numero brutto, ma 7 (che ha un fattore primo pari a 7) non lo è.

def ugly_number(num: int) -> bool:
    while num > 1:
        if num % 2 == 0:
            num //= 2
        elif num % 3 == 0:
            num//= 3 
        elif num % 5 == 0:             
            num //= 5
        else:
            return False
    return True


print(ugly_number(1))

#Immagina di avere una raccolta di note musicali rappresentate da una serie di numeri interi.
# Queste note possono avere altezze (valori) diversi.
# Una sequenza armoniosa è come una melodia piacevole in cui la differenza di altezza tra 
# la nota massimale e quella minimale è uguale a 1. 
# Ad esempio, la serie di note [3,2,2,2,3] è armoniosa, perché la differenza fra 3 e 2 è 1.

# Trovare l'armonia perfetta:

# Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri).
# La funzione dovrebbe trovare la sequenza armoniosa più lunga che puoi creare da queste note.
# Ricorda, una sottosequenza è una selezione di note dalla lista originale che mantiene l'ordine degli elementi.

# Colpire le note giuste:

# Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], la sottosequenza armonica più lunga è [3, 2, 2, 2, 3]. 
# La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza).

def find_lhs(nums: list[int]) -> int:
    numeri = []
    lista_2 = [0]
    stesso_numero = True
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] - nums[j] in [0,1]:
                if nums[i]-nums[j] == 1:
                    stesso_numero = False
                numeri.append(nums[j])
        if len(numeri) > 1 and stesso_numero == False:
            lista_2.append(len(numeri))
        numeri = []
    return max(lista_2)
print(find_lhs([1,3,2,2,5,2,3,7]))

# Date due stringhe note e magazine, restituisci true se note può essere costruita utilizzando le lettere di magazine 
# e false in caso contrario. 
# Ogni lettera nella magazine può essere utilizzata solo una volta in note.

def ransom(note: str, magazine: str) -> bool:
    magazine_letters = {letter: magazine.count(letter) for letter in set(magazine)}
        
    for letter in note:
        if letter not in magazine_letters or magazine_letters[letter] == 0:
            return False
        magazine_letters[letter] -= 1
    return True
    
ransom("a", "b")
ransom("aa", "ab")
ransom("aa","aab")