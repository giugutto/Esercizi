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
    for i in range(70):
        if i == tartaruga_pos:
            print("T", end=" ")
        elif i == lepre_pos:
            print("H", end=" ")
        elif i == lepre_pos and i == tartaruga_pos:
            print("OUCH!", end=" ")
        elif i == 0:
            print("-", end=" ")


def tartaruga_move(weather) -> int:
    x = random.randint(1, 10)
    passoveloce = 3
    passolento = -6
    scivolata = 1
    if weather == "pioggia":
        x -= 1
    if x <= 5:
        return passoveloce
    elif x <= 7:
        return scivolata
    else:
        return passolento

def lepre_move(weather):
    i = random.randint(1,10)
    riposo = 0
    grandeb = 9
    grandes = -12
    piccolob = 1
    piccolas = -2

    if i <= 2:
        return riposo
    if i <= 4:
        return grandeb
    if i <= 5:
        return grandes
    if i <= 8:
        return piccolob
    if i <= 11:
        return piccolas
    


print("'BANG !!!!! AND THEY'RE OFF !!!!!'")

lepre_pos = 1
tartaruga_pos = 1

while True:
    lepre_pos += lepre_move()
    if lepre_pos < 0:
        lepre_pos = 0
    tartaruga_pos += tartaruga_move()
    if tartaruga_pos < 0:
        tartaruga_pos = 0

    print_quadri(70, tartaruga_pos,lepre_pos)

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
