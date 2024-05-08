# definiamo una nuova classe!
class Persona:
    #il costruttore si crea così:(nome,cognome e codice fiscale sono attributi)
    def __init__(self, name:str , surname:str) -> None:
        #nb, ID non è stato messo nei parametri
        #mettiamo un underscore se vogliamo che gli attributi non vengano cambiati
        #per gli attributi privati un getter ritorna i valori(return, self.x) e setter consente di modificarle

        self._ID: int = 1
        self._name: str = name
        self._surname: str = surname
        self._birthdate: str = "12/03/2002"
        self._birth_place: str = "Napoli"
        self._gender: str = "M"
        self._ssn = None
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
    #raise Exception("you can't do it!")

    def compute_ssn(self) -> str:
        primelettere = "" 
        for i in self._name:
            if i in "bcdfghlmnpqrstvz":               
                primelettere += i
            else:
                continue
        first_three_character_name = primelettere[0] + primelettere[2] + primelettere[3]
        primeletterecognome = "" 
        for i in self._surname:
            if i in "bcdfghlmnpqrstvz":                               
                primeletterecognome += i
            else:
                continue
        first_three_character_surname = primeletterecognome[:3]
        year = self._birthdate[-2:]
        if self._birthdate[3:5] == "01":
            month = "A"
        if self._birthdate[3:5] == "02":
            month = "B"
        if self._birthdate[3:5] == "03":
            month = "C" 
        if self._birthdate[3:5] == "04":
            month = "D" 
        if self._birthdate[3:5] == "05":
            month = "E"
        if self._birthdate[3:5] == "06":
            month = "H"
        if self._birthdate[3:5] == "07":
            month = "L"
        if self._birthdate[3:5] == "08":
            month = "M" 
        if self._birthdate[3:5] == "09":
            month = "P" 
        if self._birthdate[3:5] == "10":
            month = "R" 
        if self._birthdate[3:5] == "11":
            month = "S"
        if self._birthdate[3:5] == "12":
            month = "T" 
        day = self._birthdate[:2]
        if self._gender == "F":
            day = self._birthdate[:2] + 40
        if self._birth_place == "L'aquila":
            city = "A345" 
        if self._birth_place == "Ancona":
            city = "A271"       
        if self._birth_place == "Aosta":
            city = "A326" 
        if self._birth_place == "Bari":
            city = "A662"
        if self._birth_place == "Bologna":
            city = "A944" 
        if self._birth_place == "Cagliari":
            city = "B354"    
        if self._birth_place == "Campobasso":
            city = "B519" 
        if self._birth_place == "Catanzaro":
            city = "C352"       
        if self._birth_place == "Firenze":
            city = "D612" 
        if self._birth_place == "Genova":
            city = "D969"       
        if self._birth_place == "Milano":
            city = "F205"
        if self._birth_place == "Napoli":
            city = "F839"
        if self._birth_place == "Palermo":
            city = "G273"
        if self._birth_place == "Perugia":
            city = "G478"
        if self._birth_place == "Potenza":
            city = "G942"
        if self._birth_place == "Roma":
            city = "H501"
        if self._birth_place == "Torino":
            city = "L219"
        if self._birth_place == "Trento":
            city = "L378"
        if self._birth_place == "Trieste":
            city = "L424"
        if self._birth_place == "Venezia":
            city = "L736"

        self._ssn = first_three_character_surname.upper() + first_three_character_name.upper() + year + month + day + city




#andiamo a creare oggetto/istanza
persona_1: Persona = Persona(name="giuseppe", surname="guttoriello",)
persona_1.compute_ssn()
print(persona_1.get_ssn())


#persona_1.setname(name="peppe")

#print(persona_1.get_name())

# persona_2: Persona = Persona(name="Valentino", surname="Rossi", ssn="VLTRSS")
# persona_2.set_ssn("HFISDJD")
# print(persona_2.get_ssn())
# queue: list[Persona] = [persona_1,persona_2]
# for i in queue:
#     print(i.get_cf())


