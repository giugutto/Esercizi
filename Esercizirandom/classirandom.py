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



magazzino = GestoreMagazzino(0)
prodotto1 = Prodotto("Kendama", 15, 78)
prodotto2 = Prodotto("Boomerang", 12, 23)
magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
print(magazzino.prodotti)