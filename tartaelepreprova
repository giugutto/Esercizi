import random
# In questo problema ricreerete la classica gara tra la tartaruga e la lepre.
# Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento.
# I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati.
# Ogni quadrato rappresenta una posizione lungo il percorso della corsa.
# Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara.
# Durante la corsa, i contendenti possono occasionalmente perdere terreno.
# C'è un orologio che conta i secondi. Ad ogni tick dell'orologio,
# il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

# - Tartaruga:
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato.

# - Lepre:
#     - Riposo (20% di probabilità): non si muove.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
#     -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

# Il percorso è rappresentato attraverso l'uso di una lista.
# Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70).
# Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza").
# Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.
# Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10.
# Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5,
# una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10.
# Usate una tecnica simile per muovere la lepre seguendo le sue regole.
# Iniziate la gara stampando:
# 'BANG !!!!! AND THEY'RE OFF !!!!!'
# Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo),
# stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga,
# la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere.
# Occasionalmente, i contendenti si troveranno sullo stesso quadrato.
#In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione.
# Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.
# Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così,
# stampate il nome del vincitore e terminate la simulazione.
# Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!".
# Se vince la lepre, stampate "HARE WINS || YUCH!!!".
# Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"),
# oppure stampare "IT'S A TIE.".
# Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

# Requisiti del Codice:
# - Utilizzare il modulo random per la generazione dei numeri casuali.
# - Definire e utilizzare:
#     - una funzione per visualizzare le posizioni sulla corsia di gara,
#     - una funzione per calcolare la mossa della tartaruga,
#     - una funzione per calcolare la mossa della lepre.
# - Implementare un loop per simulare i tick dell'orologio.
# Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.



def print_quadri(position, lepre_pos, tartaruga_pos):
    for i in range(1, 71):
        if i == tartaruga_pos:
            print("T", end=" ")
        elif i == lepre_pos:
            print("H", end=" ")
        elif i == lepre_pos and i == tartaruga_pos:
            print("OUCH!", end=" ")
        else:
            print("-", end=" ")

#ogni 10 tick dell'orologio.
def tartaruga_move(weather, energy) -> int:
    x = random.randint(1, 10)
    passoveloce = 3
    passolento = -6
    scivolata = 1
    if weather == "Pioggia": 
        x -= 1
    if x <= 5:
        if energy >= 5:
            energy -= 5
            return passoveloce, energy
        else:
            energy += 10
            return 0, energy
    elif x <= 7:
        if energy >= 10:
            energy -= 10
            return scivolata, energy
        else:
            energy += 10
            return 0, energy    
    else:
        if energy >= 3:
            energy -= 3
            return passolento, energy
        else:
            energy += 10
            return 0, energy    
    

def lepre_move(weather, energy):
    i = random.randint(1,10)
    riposo = 0
    grandeb = 9
    grandes = -12
    piccolob = 1
    piccolas = -2
    if weather == "Pioggia":
        i -= 2 
    if i <= 2:
        energy = min(100, energy + 10)
        return 0, energy
    if i <= 4:
        if energy >= 15:
            energy -= 15
            return grandeb, energy
        else:
            return 0, energy
    if i <= 5:
        if energy >= 20:
            energy -= 20
            return grandes, energy
        else:
            return 0, energy
    if i <= 8:
        if energy >= 5:
            energy -= 5
            return piccolob, energy
        else:
            return 0, energy
    if i <= 11:
        if energy >= 8:
            energy -= 8
            return piccolas, energy
        else:
            return 0, energy
        
       
def change_weather(tick):
    if tick % 10 == 0:
        return random.choice(["soleggiato", "pioggia"])
    else:
        return None

print("'BANG !!!!! AND THEY'RE OFF !!!!!'")

lepre_pos = 1
tartaruga_pos = 1

tartaruga_energia = 100
lepre_energia = 100

tick = 0
weather = "soleggiato"

while True:
    tick += 1
    weather = change_weather(tick) or weather #se non c'è nessun cambiamento lascia il meteo corrente
    Ostacoli:dict = {15: -3, 30: -5, 45: -7}
    Bonus:dict = {10: 5, 25: 3, 50: 10}
    lepre_move_result, lepre_energia = lepre_move(weather, lepre_energia)
    lepre_pos += lepre_move_result

    for k,v in Ostacoli.items():
        if lepre_pos == k:
            lepre_pos - v
        else:
            continue
    for k,v in Bonus.items():
        if lepre_pos == k:
            lepre_pos + v
        else:
            continue
    if lepre_pos < 0:
        lepre_pos = 0
    tartaruga_move_result, tartaruga_energia = tartaruga_move(weather, tartaruga_energia)
    tartaruga_pos += tartaruga_move_result
    for k,v in Ostacoli.items():
        if tartaruga_pos == k:
            tartaruga_pos -= v
        else:
            continue
    for k,v in Bonus.items():
        if tartaruga_pos == k:
            tartaruga_pos += v
        else:
            continue
    if tartaruga_pos < 0:
        tartaruga_pos = 0
    # Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45),
# gli ostacoli riducono la posizione dell'animale di un numero specificato di quadrati (es: -3, -5, -7).
# Gli ostacoli sono rappresentati da un dizionario che mappa le posizioni degli ostacoli sul percorso
# (chiave) ed i relaviti effetti (valore).
# Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito di un ostacolo.

    print_quadri(70, lepre_pos,tartaruga_pos)

    if lepre_pos >= 70 and tartaruga_pos >= 70:
        print("IT'S A TIE!!")
        break
    elif lepre_pos >= 70:
        print("LEPRE WINS || YUCH!!")
        break
    elif tartaruga_pos >= 70:
        print("TARTARUGA WINS! || VAY!")
        break

# SFIDE AGGIUNTIVE:
# 1. Variabilità Ambientale:
# Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
# Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti.
# Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.

# Modificatori mossa:
# - La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
# - La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.

# 2. Energia o Stamina:
# Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni.
# Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia.
# L'energia inziale per entrambi gli animali è 100.

# Nuove regole di movimento:
# - Tartaruga:
#     - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia,
# essa guadagna 10 di energia. Non può superare l'energia iniziale.
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

# - Lepre:
#     - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energia iniziale.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia.
# Non può andare sotto il quadrato 1.
#     - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia.
# Non può andare sotto il quadrato 1.

# 3. Ostacoli e Bonus
# Sulla pista di gara sono presenti alcuni ostacoli e bonus a posizioni fisse,
# che influenzano direttamente il movimento degli animali quando vengono calpestati.
# Gli ostacoli causano uno slittamento all'indietro, mentre i bonus offrono un avanzamento extra.

# Dettagli Implementativi:
# - Ostacoli:
# Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45),
# gli ostacoli riducono la posizione dell'animale di un numero specificato di quadrati (es: -3, -5, -7).
# Gli ostacoli sono rappresentati da un dizionario che mappa le posizioni degli ostacoli sul percorso
# (chiave) ed i relaviti effetti (valore).
# Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito di un ostacolo.
Ostacoli:dict = {15: -3, 30: -5, 45: -7}

# - Bonus:
# Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50),
# i bonus aumentano la posizione dell'animale di un numero determinato di quadrati (es: 5, 3, 10).
# I bonus sono rappresentati da un dizionario che mappa le posizioni dei bonus sul percorso
# (chiave) ed i relaviti effetti (valore).
# Consentire agli animali di beneficiare pienamente dei bonus, ma non oltrepassare il traguardo.

Bonus:dict = {10: 5, 25: 3, 50: 10}