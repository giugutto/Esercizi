# definiamo una nuova classe!
class Persona:
    #il costruttore si crea così:(nome,cognome e codice fiscale sono attributi)
    def __init__(self, name:str , surname:str, ssn:str) -> None:
        #nb, ID non è stato messo nei parametri
        #mettiamo un underscore se vogliamo che gli attributi non vengano cambiati
        #per gli attributi privati un getter ritorna i valori(return, self.x) e setter consente di modificarle

        self._ID: int = 1
        self._name: str = name
        self._surname: str = surname
        self._ssn: str =ssn
        self._birthdate: str = "17/09/1996"
        self.birth_place: str = "Roma"
        self._gender: str = "M"
        #funzioni della classe 
    def get_name(self):
        '''
        questa funziona stampa il nome della persona
        name: str
        return: self._name
        '''
        return self._name
    def setname(self, name:str) -> None:
        '''
        setter, this function seet the attribute name
        input: name : str, the paameter contains the user's name
        return: None
        '''
        raise Exception("You can't change the name!")
    def get_ssn(self) -> str:
        '''
        questa funzione legge il codice fiscale dell'utente
        tipo: str
        return: str
        '''
        return self._ssn 
    # def set_ssn(self, ssn: str) -> None:
    #     '''
    #     this function allow to set the ssn
    #     type:str
    #     return:str
    #     '''       
    #     self._ssn = ssn
    def set_ssn(self, ssn: str) -> None:
         '''
         this function allow to set the ssn
         type:str
         return:str
         '''       
    raise Exception("you can't do it!")

#andiamo a creare oggetto/istanza
persona_1: Persona = Persona(name="Giuseppe", surname="Guttoriello", ssn="GTTGPP")

print(persona_1.get_name())


#persona_1.setname(name="peppe")

#print(persona_1.get_name())

persona_2: Persona = Persona(name="Valentino", surname="Rossi", ssn="VLTRSS")
persona_2.set_ssn("HFISDJD")
print(persona_2.get_ssn())
# queue: list[Persona] = [persona_1,persona_2]
# for i in queue:
#     print(i.get_cf())

def check_ssn(self, ssn:str)-> bool:
    '''
    calcola l'ssn della pesrona
    '''