from Paziente import Paziente
from Dottore import Dottore

### CLASSE: Fattura
# Creare un file chiamato "fatture.py".
# In tale file, creare una classe chiamata Fattura.

class Fattura:
    def __init__(self, pazienti: list[Paziente], doctor: Dottore) -> None:
        
        if doctor.isAValidDoctor():
            self.__pazienti = pazienti
            self.__doctor = doctor
            self.__fatture = len(self.__pazienti)
            self.__salary = 0
        else:
            self.__pazienti = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        self.__salary = self.__doctor.getParcel() * len(self.__pazienti)
        return self.__salary
    
    def getFatture(self):
        self.__fatture = len(self.__pazienti)
        return self.__fatture
    
    def addPatient(self, newpatient: Paziente):
        if newpatient not in self.__pazienti:
            self.__pazienti.append(newpatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Doctor {self.__doctor.getLastname()}, è stato aggiunto il paziente {newpatient.getidCode()}")
    
    def removePatient(self, id_to_remove):
        for i in self.__pazienti:
            if i.getidCode() == id_to_remove:
                self.__pazienti.remove(i)
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Doctor {self.__doctor.getLastname()}, è stato rimosso il paziente {i.getidCode()}")

        


        


        
# - Definire i seguenti metodi:

#     init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
#     getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
#     getFatture(): deve ritornare il valore dell'attributo fatture, dopo aver assegnato ad esso il numero dei pazienti che ha il dottore.
#     addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
#     removePatient(): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
