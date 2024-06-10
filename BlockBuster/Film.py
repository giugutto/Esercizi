class Film: #rappresenta film preso a noleggio
    def __init__(self) -> None:
        self.__id: int
        self.__titolo: str
    

    def setID(self, id: int):
        self.__id = id
    
    def setTitle(self,title):
        self.__titolo = title

    def getID(self):
        return self.__id
    
    def getTitle(self):
        return self.__titolo
    
    def isEqual(self,otherFilm: 'Film'):
        if self.__id == otherFilm.__id:
            return True

### CLASSE: Film
# In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
 
# - Definire i seguenti metodi:
# init(id, title): metodo costruttore.
# setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
# setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
# getID(): che consente di ritornare il valore del codice identificativo di un film.
# getTitle(): che consente di ritornare il valore del titolo di un film.
# isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
 