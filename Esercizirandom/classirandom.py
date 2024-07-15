# Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”.
# Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e un metodo 
# “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, 
# ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.

class Impiegato:
    def __init__(self, nome:str,cognome:str,matricola:int,stipendio:int) -> None:
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio

    def aumenta_stipendio(self):
        self.stipendio = self.stipendio + self.stipendio * 10 / 100
    
    def stampa_dettagli(self):
        print(f"Il nome dell'impegato è {self.nome}, il cognome dell'impiegato è {self.cognome}, con matricola {self.matricola} e il suo stipendio è di {self.stipendio} euro.")

impiegato1 = Impiegato("Marco","Rossi",12345,3000)

impiegato1.stampa_dettagli()
impiegato1.aumenta_stipendio()
impiegato1.stampa_dettagli()


# Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
# Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
# Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
# La classe dovrà avere i seguenti metodi:
# Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
# Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
# Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
# Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.
class Prodotto:
    def __init__(self, nome: str, prezzo: int, scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta

class GestoreMagazzino:
    def __init__(self,costo_magazzinaggio):
        self.prodotti = {}
        self.costo_magazzinaggio = costo_magazzinaggio
    
    def aggiungi_prodotto(self, prodotto:Prodotto):
        self.prodotti[prodotto.nome] = [prodotto.nome , prodotto.prezzo , prodotto.scorta]

    def rimuovi_prodotto(self, prodottodarimuovere: Prodotto):
        self.prodotti.pop(prodottodarimuovere)

    def calcola_costi_magazzinaggio(self):
        x = 0        
        for i in self.prodotti:
            x += i.prezzo
        self.costo_magazzinaggio = x

    def show_prodotti(self):
        print(self.prodotti)



# magazzino = GestoreMagazzino(0)
# prodotto1 = Prodotto("Kendama", 15, 78)
# prodotto2 = Prodotto("Boomerang", 12, 23)
# magazzino.aggiungi_prodotto(prodotto1)
# magazzino.aggiungi_prodotto(prodotto2)
#print(magazzino.prodotti)
'''
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.'''

class Prodotto:
    def __init__(self, nome: str, quantita: int):
        self.nome = nome
        self.quantita = quantita
        
class Magazzino:
    def __init__(self, magazzino: list = []):
        self.magazzino = magazzino
    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.magazzino.append(prodotto)
        
    def cerca_prodotto(self, nome: str):
        for i in self.magazzino: #Nota bene, dal momento che questo metodo fa parte della classe Magazzino, noi possiamo accedere al suo attributo "prodotti"
            if i.nome == nome: #Dal momento che l'attributo "prodotti" è una lista di elementi che fanno parte della classe prodotto, noi possiamo accedere ai suoi attributi.
                return i
    #def verifica_disponibilita(self, nome:str):
        

# magazzino =(Magazzino)
# magazzino.aggiungi_prodotto("Pomodori", 23)
# magazzino.cerca_prodotto("Pomodori")




# '''Progettare un semplice sistema bancario con i seguenti requisiti:
# Classe del Account:
# Attributi:
# account_id: str - identificatore univoco per l'account.
# balance: float - il saldo attuale del conto.
# Metodi:
# deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
# get_balance(): restituisce il saldo corrente del conto.
# Classe Bank:
# Attributi:
# accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
# Metodi:
# create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
# deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
# get_balance(account_id): restituisce il saldo del conto con l'ID specificato.'''

class Account:
    def __init__(self,account_id: str, balance: float):
        self.account_id = account_id
        self.balance = balance
    def deposit(self, amount: float):
        self.balance += amount
    def get_balance(self):
        return f"L'ammmontare del tuo saldo è di {self.balance}"
    

class Bank:
    def __init__(self):
        self.account = {}
    def create_account(self, account_id):
        self.account[account_id] = 0
    def deposit(self, account_id, amount):
        for k,v in self.account.items():
            if k == account_id:
                self.account[k] = amount
    def get_balance(self, account_id):
        for k in self.account:
            if k == account_id:
                return self.account[k]
            
account1 = Account("ciccio", 123.32)
account1.deposit(342)
print(account1.get_balance())

banca = Bank()
banca.create_account("pippo")
banca.deposit("pippo",1012)
print(banca.get_balance("pippo"))

'''
Obiettivo
L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni di due specie animali usando la programmazione orientata agli oggetti in Python.

Descrizione del problema
Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
Specifiche tecniche
1. Classe Specie

- Attributi:
nome (str): Nome della specie.
popolazione (int): Popolazione iniziale.
tasso_crescita (float): Tasso di crescita annuo percentuale.
- Metodi:
__init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per inizializzare gli attributi della classe.
cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².
'''

class Specie:
    def __init__(self,nome, popolazione: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        self.popolazione = (self.popolazione * (1 + self.tasso_crescita/100))//1
        

    def anni_per_superare(self, altra_specie:'Specie')-> int:
        #METTITI IN TESTA CHE QUANDO METTIAMO UN ATTRIBUTO DI UNA CLASSE POSSIAMO USARE I SUOI ATTRIBUTI
        variabilecontatore = 0
        while variabilecontatore < 1000 and self.popolazione < altra_specie.popolazione:
            self.cresci()
            altra_specie.cresci()
            variabilecontatore +=1
        return variabilecontatore    
        

    def getDensita(self, area_kmq: float):
        variabilecontatore =  0
        while variabilecontatore <= 1000 and self.popolazione / area_kmq < 1:
            self.cresci()
            variabilecontatore += 1            
        return variabilecontatore

    
        
class BufaloKlingon(Specie):
    def __init__(self,popolazione: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione, tasso_crescita)


class Elefante(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__("Elefante",popolazione, tasso_crescita)
        









'''
2. Sottoclassi BufaloKlingon e Elefante

Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:
Aggiornamento della popolazione per l'anno successivo:
Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
Calcolo della densità di popolazione:
Formula: popolazione / area_kmq
Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
Calcolo degli anni necessari per superare la popolazione di un'altra specie:
Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di questa specie non supera quella dell'altra.
'''

