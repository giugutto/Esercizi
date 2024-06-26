# Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato.
# La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

# Classe Contatore
# Attributi:
# - conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

# Metodi:
# - __init__(): Inizializza l'attributo conteggio a 0.
# - setZero(): Imposta il conteggio a 0.
# - add1(): Incrementa il conteggio di 1.
# - sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
# - get(): Restituisce il valore corrente del conteggio.
# - mostra(): Stampa a schermo il valore corrente del conteggio.

class Contatore:
    def __init__(self) -> None:
        self.contatore = 0 #quando non dichiariamo un attributo all'interno delle parentesi,
                            #possiamo farlo qui sotto, in modo che l'attributo non abbia un valore costante

    def setZero(self):
        self.contatore = 0

    def add1(self):
        self.contatore += 1

    def sub1(self):
        if self.contatore == 0:
            print("Non è possibile eseguire la sottrazione")
        else:
            self.contatore -= 1
    def get(self):
        return self.contatore
    
    def mostra(self):
        print(f"Conteggio attuale: {self.contatore}")




# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, 
# modificare, e cercare ricette basate sugli ingredienti. 
# Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.

#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti.
#     Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.

#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. 
#     Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
#     Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): 
#     Sostituisce un ingrediente con un altro nella ricetta specificata. 
#     Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - list_recipes(): Elenca tutte le ricette esistenti.

#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. 
# Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

#     - search_recipe_by_ingredient(ingredient): 
# Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
# Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

class RecipeManager:
    def __init__(self):
        self.ricettario = {}

    def create_recipe(self, name: str, ingredients: list):
        if name in self.ricettario:
            return "La ricetta esiste già"
        else:
            self.ricettario[name] = ingredients
            return self.ricettario
        
    def add_ingredient(self, recipe_name, ingredient: str): #Aggiunge un ingrediente alla ricetta specificata. 
        if ingredient in self.ricettario or recipe_name not in self.ricettario:
            return " L'ingrediente esiste già o la ricetta non esiste"
        else:  
            self.ricettario[recipe_name].append(ingredient)    
            return self.ricettario

        #Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
    def remove_ingredient(self, recipe_name, ingredient):
        for i,recipe in enumerate(self.ricettario[recipe_name]):
            if recipe == ingredient:
                del self.ricettario[recipe_name][i]
                return self.ricettario
                
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if old_ingredient not in self.ricettario[recipe_name]:
                return "L'ingrediente non è presente"
        for i in range(len(self.ricettario[recipe_name])):
            if self.ricettario[recipe_name][i] == old_ingredient:
                self.ricettario[recipe_name][i]= new_ingredient
                return self.ricettario
            else:
                continue
            
            
            
    def list_recipes(self): #Elenca tutte le ricette esistenti.
        chiavi = []
        for i in self.ricettario:
            chiavi.append(i)
            return chiavi
    def list_ingredients(self, recipe_name):
        if recipe_name in self.ricettario:
            return self.ricettario[recipe_name]
        else:
            return "La ricetta non esiste"
        
    def search_recipe_by_ingredient(self, ingredient):
        
        ricetta = {}
        for chiavi in self.ricettario: #prende le chiavi del dizionario
            for i in range(len(self.ricettario[chiavi])):#prende i valori delle liste nel dizionario
                if self.ricettario[chiavi][i] == ingredient:
                    ricetta = self.ricettario
                    return ricetta
            else:
                return "Nessuna ricetta contiene questo ingrediente"




# manager = RecipeManager()
# print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
# print(manager.add_ingredient("Pizza Margherita", "Basilico"))
# print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
# print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
# print(manager.list_ingredients("Pizza Margherita"))
# print(manager.search_recipe_by_ingredient("Pomodoro"))



# In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.

# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
# Attributi:
# marca (stringa)
# modello (stringa)
# anno (intero)
# Metodi:
# __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
# descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato
# "Marca: [marca], Modello: [modello], Anno: [anno]".

class Veicolo:
    def __init__(self, marca:str, modello:str, anno:int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int): #aggiungiamo un attributo a quelli già presenti della superclasse
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
        #Qui sopra sovrascriviamo il metodo "descrivi_veicolo" della superclasse

class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")


# Obiettivo
# L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni di due specie animali usando la programmazione orientata agli oggetti in Python.

# Descrizione del problema
# Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. 
#Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
# - In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
# - n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
# Specifiche tecniche:
# 1. Classe Specie

# - Attributi:
# nome (str): Nome della specie.
# popolazione (int): Popolazione iniziale.
# tasso_crescita (float): Tasso di crescita annuo percentuale.
# - Metodi:
# __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): 
# Costruttore per inizializzare gli attributi della classe.
# cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
# anni_per_superare(self, altra_specie: 'Specie') -> int: 
# Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
# getDensita(self, area_kmq: float) -> int: 
# Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².
class Specie:
    def __init__(self,nome, popolazione: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        self.popolazione = (self.popolazione * (1 + self.tasso_crescita/100))//1
        

    def anni_per_superare(self, altra_specie:'Specie')-> int:
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
        



        


#Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²

# 2. Sottoclassi BufaloKlingon e Elefante

# Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e 
# devono inizializzare il nome della specie rispettiva.
# Formule Matematiche:
# Aggiornamento della popolazione per l'anno successivo:
# Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
# Calcolo della densità di popolazione:
# Formula: popolazione / area_kmq
# Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
# Calcolo degli anni necessari per superare la popolazione di un'altra specie:
# Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione 
# di questa specie non supera quella dell'altra.
