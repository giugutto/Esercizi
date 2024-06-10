import unittest
from Person import Person
from Fatture import *
from Paziente import *
from Dottore import *
### Creazione di Test Case con UnitTest

# Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
# Istruzioni
# Creare un nuovo file Python denominato "test_persona.py".
# Importare il modulo unittest e tutte le classi definite.

# Test della Classe Persona
# - Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi first_name, last_name e age.
#   - Il funzionamento dei metodi setName, setLastName e setAge.

class testPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.Person = Person("MariaAngela","Ciccina")

    def testInizialization(self):
        self.assertEqual(self.Person.__first_name, "MariaAngela")
        self.assertEqual(self.Person.__last_name, "Ciccina")
        self.assertEqual(self.Person.__age, 0)

    def test_SetName(self):
        self.Person.set_name("Mario")
        self.assertEqual(self.Person.__first_name, "Mario")

    def test_SetName(self):
        self.Person.setLastName("Bibbio")
        self.assertEqual(self.Person.__last_name, "Bibbio")

    def test_SetName(self):
        self.Person.setAge(0)
        self.assertEqual(self.Person.__age, 0)

    


        


# Test della Classe Dottore
# - Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi specifici di Dottore.
#   - Il funzionamento del metodo isValidDoctor con diverse età.





# Test della Classe Paziente
# - Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi specifici di Paziente.

# Test della Classe Fattura
# - Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta della classe Fattura.
#   - Il calcolo corretto del salario e del numero di fatture.
#   - L'aggiunta e la rimozione di pazienti dalla lista.
