from Person import Person

# ### CLASSE: Paziente
# Creare un file chiamato "paziente.py".
# In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

class Paziente(Person):
    def __init__(self, first_name: str, last_name: str, idCode: str):
        super().__init__(first_name, last_name)
        self.__idCode = idCode

    
    def setIDCode(self, idcode):
        self.__idCode = idcode

    def getidCode(self):
        return self.__idCode
    def patientInfo(self):
        print(f"Paziente: {self.__first_name} {self.__last_name}\nID: {self.__idCode}")

# Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
# - Definire i seguenti metodi:

#     costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
#     setIdCode(idCode): consente di impostare il codice identificativo del paziente.
#     getidCode(): consente di ritornare il codice identificativo del paziente.
#     patientInfo(): stampa in output le informazioni del paziente in questo modo:

#         "Paziente: {nome} {cognome}
#          ID: {codice identificativo}"