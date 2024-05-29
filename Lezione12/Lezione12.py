# <!-- Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
# Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli,
# restituirli e visualizzare quali libri sono disponibili in un dato momento.

# Classi:
# - Libro: Rappresenta un libro con titolo, autore, stao del prestito. Il libro deve essere inizialmente disponibile (non prestato).

# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#     Metodi:
#     - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

#     - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

#     - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

#     - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

# Test Cases:
# - Un amministratore della biblioteca aggiunge alcuni libri all'inventario.

# - Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.

# - L'utente restituisce il libro, che viene marcato di nuovo come disponibile.

# - In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
# Last modified: Wednesday, 29 May 2024, 11:28 AM -->
#- Libro: Rappresenta un libro con titolo, autore, stao del prestito. Il libro deve essere inizialmente disponibile (non prestato).
class Libro:
    def __init__(self, titolo:str, autore:str,) -> None:
        self.titolo = titolo
        self.autore = autore
        self.stato_del_prestito:bool = False
    
class Biblioteca:
    def __init__(self) -> None:
        self.libri: list[Libro] = []

    def aggiungi_libro(self, libro:Libro):
        if libro not in self.libri:
            self.libri.append(libro)
            return f"{libro.titolo} è stato aggiunto alla biblioteca"
        else:
            return "Il libro è già nella biblioteca"

    def presta_libro(self, titolo:str):
       for i in self.libri:
        if titolo == i.titolo:
            if not i.stato_del_prestito:
                i.stato_del_prestito = True
                return f"{titolo} è stato prestato"
            else:
                return f"{titolo} è stato già prestato"
        else:
            return "Il libro non è presente nella biblioteca"

    def restituisci_libro(self, titolo:str):
        for i in self.libri:
            if i.titolo == titolo and i.stato_del_prestito == True:
                i.stato_del_prestito = False
                return f"{titolo} è stato restituito"
            else:
                return "Il libro è presente nella libreria ed è stato prestato"

    def mostra_libri_disponibili(self):
        libri_disponibili: list[Libro] = [libro.titolo for libro in self.libri if libro.stato_del_prestito == False]
        return libri_disponibili if libri_disponibili else "Errore: nessun libro disponibile"
    

biblioteca = Biblioteca()
libro1 = Libro("HP - E la pietra filosofale", "JK Rowling")
libro2 = Libro("Topolino","mazzancolla")

print(biblioteca.aggiungi_libro(libro1))
print(biblioteca.aggiungi_libro(libro2))
print(biblioteca.presta_libro(libro1.titolo))
print(biblioteca.mostra_libri_disponibili())
print(biblioteca.restituisci_libro(libro1.titolo))



# Catalogo Film 
# Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere,
# rimuovere e cercare film di un particolare regista.
# Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

# Classe:
# - MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.

#     Metodi:
#     - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
# Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

#     - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista.
# Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

#     - list_directors(): Elenca tutti i registi presenti nel catalogo.

#     - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

#     - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
# Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
# Last modified: Wednesday, 29 May 2024, 11:52 AM

class Moviecatalog:
    def __init__(self):
        self.catalog: dict = {}

    def add_movie(self, director_name:str, movies: list):
        if director_name not in self.catalog:
            self.catalog[director_name] = [movies]
        else:
                self.catalog[director_name].append(movies)

    def remove_movie(self,director_name: str, movie_name: str):
        if director_name in self.catalog:
            self.catalog[director_name].remove(movie_name)
            if self.catalog[director_name] == []:
                del self.catalog[director_name]
    
    def list_directories(self):
        print(self.catalog.keys())

    def get_movies_by_director(self, director_name):
        print(self.catalog[director_name])
            
    def search_movies_by_titles(self, title: str):
            x = []
            for director in self.catalog:
                film: list[str] = self.catalog[director]
                for i in film:
                    if title.lower() in i.lower():
                        if director not in x:
                            x.append(director)
                        x.append(i)
            if x:
                return x
            else:
                print("Error, there's no title that match this word")
                

        
catalogo = Moviecatalog()
catalogo.add_movie("Roberto Benigni", "La vita è bella")
catalogo.add_movie("Roberto Benigni", "haisda")
catalogo.add_movie("Fellini", "La vita è brutta")
catalogo.get_movies_by_director("Roberto Benigni")
catalogo.add_movie("Vincenzo Salemme","E Fuori Nevica")
catalogo.remove_movie("Roberto Benigni", "haisda")
catalogo.list_directories()
print(catalogo.search_movies_by_titles("La"))
