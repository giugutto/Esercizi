# Sistema di Prenotazione Cinema

# Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. 
# Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
# Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

# Classi:
# - Film: Rappresenta un film con titolo e durata.
# - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
# - Cinema: Gestisce le operazioni legate alla gestione delle sale.

#     Metodi sala:
#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. 
# Restituisce un messaggio di conferma o di errore.
#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.


#     Metodi cinema:
#     - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. 
# Restituisce un messaggio di stato.

# Test case:
# - Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.

# - Un cliente sceglie un film e prenota un certo numero di posti.

# - Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

class Film:
    def __init__(self, titolo, durata) -> None:
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, id, film:Film, posti_totali, posti_prenotati) -> None: #essendo una costante, avremmo dovuto mettere l'attributi posti prenotati sotto all'init(costruttore)
        self.id = id
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = posti_prenotati

    def prenota_posti(self, num_posti):
        posti_disponibili = self.posti_totali - self.posti_prenotati
        if num_posti <= posti_disponibili:
            print("i tuoi posti sono stati prenotati")
            self.posti_prenotati += num_posti
        else:
            print("Mi dispiace, i posti che vuoi prenotare non sono disponibili")

    def posti_disponibili(self):
        print(self.posti_totali - self.posti_prenotati)

class Cinema:
    def __init__(self, sale = []) -> None:
        self.sale: list[Sala] = sale

    def aggiungi_sala(self,sala:Sala):
        self.sale.append(sala)
    
    def prenota_film(self, titolo_film, num_posti):
        for x in self.sale:
            if x.film.titolo == titolo_film:
                x.prenota_posti(num_posti)
            



film1 = Film("La vita è bella", "2h 50m")
film2 = Film("Fast&Furious", "2h 30m")
film3 = Film("ET", "2h 50m")
film4 = Film("Harry Potter e la pietra filosofale", "2h 10m")

sala1 = Sala("12", film1,100, 4)
sala2 = Sala("9", film2,80, 56)
sala3 = Sala("92",film3, 120, 60)

cinema = Cinema([sala1,sala2])

cinema.aggiungi_sala(sala3)
cinema.prenota_film("La vita è bella", 9)


# Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino,
# cercare prodotti per nome e verificare la disponibilità di un prodotto.

# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)
 
# Definisci una classe Magazzino con i seguenti metodi:
# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.

class Prodotto:
    def __init__(self, nome: str, quantity: int) -> None:
        self.nome = nome
        self.quantity = quantity

class Magazzino:
    def __init__(self, prodotti:list = []) -> None:
        self.prodotti = prodotti

    def aggiungi_prodotto(self, prodotto:Prodotto):
        self.prodotti.append(prodotto)

    def cerca_prodotti(self, nome:str):
        self.nome = nome
        if nome in self.prodotti:
            print("Il prodotto è presente")
        else:
            print("Il prodotto non è presente")

    def verifica_disponibilita(self, nome:str):
        self.nome = nome
        if self.nome



        