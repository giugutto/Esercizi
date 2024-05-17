
# Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
# - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
#ESEMPIO:
# print(transform(4))
# 2
# print(transform(-10))
# -5

def transform(x: int) -> int:
    if x % 2 == 0:
        return int(x / 2)
    else:
        return x *  3 - 1
    
print(transform(12))


# Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. 
# L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" 
# la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
# Per ogni operaio, 
# viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
# La vostra funzione deve ricevere questa informazione per ogni impiegato e 
# determinare e stampare lo stipendio lordo.
# Result

# print(calcola_stipendio(40))
# 400.0
# print(calcola_stipendio(0))
# 0.0
def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        x = ore_lavorate * 10
        return x
    else:
        x = ore_lavorate - 40
        a = 40 * 10
        b = x * 15
        return a + b

        
#L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" 
# la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 

#  Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51
# print_seq()

	

# Sequenza a):
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# Sequenza b):
# 3
# 8
# 13
# 18
# 23

# Sequenza c):
# 20
# 14
# 8
# 2
# -4
# -10

# Sequenza d):
# 19
# 27
# 35
# 43
# 51

def print_seq(): 
    
    print("Sequenza a):")
    x = 1, 2, 3, 4, 5, 6, 7
    for i in x:
        print(i)
    print()
    print("Sequenza b):")
    x = 3, 8, 13, 18, 23
    for i in x:
        print(i)
    print()
    print("Sequenza c):")
    x = 20, 14, 8, 2, -4, -10
    for i in x:
        print(i)
    print()
    print("Sequenza d):")
    x = 19, 27, 35, 43, 51
    for i in x:
        print(i)
    
print_seq()

# Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, 
# restituisca il risultato della potenza base^exponent. 
# Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
#  La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
# Non utilizzare nessuna funzione della libreria math!

# print(integerPower(3, 4))
# 81
# print(integerPower(2, 5))
# 32

def integerPower(base:int ,esponente:int):
    if esponente != 0:
        x = base ** esponente
        return x
    

# Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo.
# La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) 
# e restituire l'ipotenusa come un float.
# Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.
#esempio
# print(hypotenuse(3.0, 4.0))
# 5.0
# print(hypotenuse(8.0, 15.0))
# 17.0

def hypotenuse(lato_1:float,lato_2:float) -> float:
    c = (lato_1 ** 2 + lato_2 ** 2) ** (0.5)
    return c


# La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
# Un errore nell'implementazione porta a risultati inaspettati.
# Trova l'errore e correggi il codice affinché soddisfi i casi di test.
# For example:
# Result
# print(calculate_average([1, 2, 3, 4, 5]))
# 3.0
# print(calculate_average([]))
# 0

# def calculate_average(numbers: list[int]) -> float:
#     if len(numbers) == 0:
#         return sum(numbers) / len(numbers)
#     else:
#         return len(numbers) / sum(numbers) - 1
    
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        x = sum(numbers) / len(numbers) 
        return x
    
print(calculate_average([1,2,3,4,5]))


# Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi 
# (ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta 
# (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).
# Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, 
# ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.
# Definire, poi, la funzione chiamata time_difference che prende come argomento due orari,
# entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la funzione seconds_since_noon 
# per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.
# Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.
#ESEMPIO
#print(time_difference(1, 0, 0, 3, 15, 30))
# 8130
# print(time_difference(0, 0, 0, 12, 0, 0))
# 43200

def seconds_since_noon(ore:int,minuti:int,secondi:int):
    return ore * 3600 + minuti * 60 + secondi

def time_difference(ora_1,minuti_1,secondi_1,ora_2,minuti_2,secondi_2):
    x = ora_1 * 3600 + minuti_1 * 60 + secondi_1
    y = ora_2 * 3600 + minuti_2 * 60 + secondi_2

    return y - x



# Si scriva una funzione in Python che simuli una palla che 
#rimbalza calcolando la sua altezza da terra in centimetri per ogni secondo,
#  a mano a mano che il tempo passa su un orologio simulato.
# Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.
# Dopo ogni secondo, il valore dell'altezza cambia, 
#aggiungendo al valore corrente dell'altezza il valore della velocità corrente; poi, 
#il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
# Dunque, dopo ogni secondo, si ha che
# altezza = altezza + velocità
# velocità = velocità - 96.
# Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, 
#si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. 
#Dunque, per il rimbalzo, si avrà che
# altezza= altezza*-0,5 
# velocità=velocità*-0,5.
# Ci si fermi al quinto rimbalzo. 
# Per ogni secondo, la funzione deve stampare il tempo trascorso e 
#l'altezza a cui si trova la palla in quel determinato secondo.
# Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
#  "Tempo: 0 Altezza: 0"
#  Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
# Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
#  "Tempo: 4 Rimbalzo!"
# For example:
# Result
# rimbalzo()
# Tempo: 0 Altezza: 0.0
# Tempo: 1 Altezza: 100.0
# Tempo: 2 Altezza: 104.0
# Tempo: 3 Altezza: 12.0
# Tempo: 4 Rimbalzo!
# Tempo: 5 Altezza: 88.0
# Tempo: 6 Altezza: 230.0
# Tempo: 7 Altezza: 276.0
# Tempo: 8 Altezza: 226.0
# Tempo: 9 Altezza: 80.0
# Tempo: 10 Rimbalzo!
# Tempo: 11 Altezza: 81.0
# Tempo: 12 Altezza: 250.0
# Tempo: 13 Altezza: 323.0
# Tempo: 14 Altezza: 300.0
# Tempo: 15 Altezza: 181.0
# Tempo: 16 Rimbalzo!
# Tempo: 17 Altezza: 17.0
# Tempo: 18 Altezza: 172.5
# Tempo: 19 Altezza: 232.0
# Tempo: 20 Altezza: 195.5
# Tempo: 21 Altezza: 63.0
# Tempo: 22 Rimbalzo!
# Tempo: 23 Altezza: 82.75
# Tempo: 24 Altezza: 245.0
# Tempo: 25 Altezza: 311.25
# Tempo: 26 Altezza: 281.5
# Tempo: 27 Altezza: 155.75
# Tempo: 28 Rimbalzo!

def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    
    # cancella pass e scrivi il tuo codice
    
    while tempo