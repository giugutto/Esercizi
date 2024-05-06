# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    return(f"Ciao {name}, buonagiornata!")

print(make_hello("Giuseppe"))


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    s_1 = string.replace(" ", "")
    return s_1
print(strip_whitespace("Ciccio      "))

# # Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# # rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# # Usare solo costrutti del linguaggio e non librerie.

def split_string(string: str, characters: str = '') -> list[str]:
    substrings = ['']
    for character in string:
        if character in characters:
            substrings += ['']
        else:
            substrings[-1] += character
    result = []
    for substring in substrings:
        if substring:
            result += [substring]
    return result

print(split_string("ciao come si va che dici","a"))
      
        


# # Scrivere una funziona che si comporta come `str.replace()`.
# # Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    result = ''
    for i in string:
        if i == find:
            result += replace
        else:
            result += i
    return result

print(replace_substring("ciao come va?", 'c', 'b'))

        
#print(replace_substring("Ciao come stai?  Spero tutto bene!", "jisldjf"))








# # Scrivere una funzione che codifica un messaggio con il cifrario di
# # Cesare, che sostituisce ad ogni carattere il carattere che si
# # trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# # si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# # La funzione permette anche di decrittare un messaggio applicando
# # l'offset in negativo. Si può assumere che il testo è minuscolo e
# # fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# # Suggerimento: Sono utili le funzioni `ord()` e `chr()`.

def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
   risultato = ''
   if decrypt == False:
       return string
   else:
    for i in string:
        x = ord(i) + offset
        risultato += x

    ciclo for, ogni lettere in stringa e convertirlo in ord e appendere al risultato chr8ord + offset 
    e se c'è il 122 ritornare ad a 97 

print(caesar_cypher("prova ciao come va tutto ok",2))
#abc diventa def se lo shifti di 3





# # Scrivere una funzione che controlla la validita' di una password.
# # La password deve avere:
# # - Almeno una lettera fra [a-z] e una lettera fra [A-Z]
# # - Almeno un numero fra [0-9]
# # - Almeno un carattere fra [$#@]
# # - Essere lunga almeno 6 caratteri
# # - Essere lunga non piu' di 16 caratteri
# # - La password non è valida se contiene caratteri diversi da quelli specificati sopra
# #   o se viola una delle regole specificate.
# # La funzione restituisce true/false a seconda se la password sia valida o meno.
# def check_pwd(pwd: str) -> bool:
#     pass
