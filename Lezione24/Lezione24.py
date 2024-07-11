'''Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.
Si crei un metodo getText() che restituisca il testo. Si crei un metodo setText() per impostare il testo. Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.'''

class Documento:
    def __init__(self, testo:str):
        self.testo = testo

    def getText(self):
        return self.testo
    
    def setText(self, newText:str):
        self.testo = newText

    def IsInText(self, parola: str) -> bool:
        if parola in self.testo:
            return True
        else:
            return False

# doc1= Documento("Prova, Gabriele è proprio bello")
# print(doc1.getText())
# print(doc1.setText("Giuseppe è bello"))
# print(doc1.IsInText("bello"))


'''Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente, il destinatario e il titolo del messaggio.
Si implementino i metodi get() e set() appropriati per tali variabili. Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.
Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
 
Da: alice@example.com, A: bob@example.com
Titolo: Incontro
Messaggio: Ciao Bob, possiamo incontrarci domani?
 
Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.'''
 
class Email(Documento):
    def __init__(self, testo):
        super().__init__(testo)
        self.mittente = None
        self.destinatario =  None
        self.titolo_del_messaggio = None

        
    
    def get_mittente(self):
        return self.mittente
    
    def get_destinatario(self):
        return self.destinatario
    
    def get_titolo_del_messaggio(self):
        return self.titolo_del_messaggio
    
    def set_mittente(self, mittente:str):
        self.mittente = mittente

    def set_destinario(self, destinatario: str):
        self.destinatario = destinatario

    def set_titolo_del_messaggio(self, titolo):
        self.titolo_del_messaggio = titolo

        
    
    
    def get_all(self):
        return f"Da: {self.mittente}, A: {self.destinatario} \n Titolo: {self.titolo_del_messaggio}, \n Messaggio:{self.getText()}"

 #RICORDA, quando ereditiamo un qualcosa se abbiamo un getter dobbiamo utilizzare il getter della classe da cui ereditiamo per prendere il messaggio!!!!!!!!!!!!!!!!!   
# email = Email("prova")

# email.set_mittente("Gabbo")
# email.set_destinario("Angelo")
# email.set_titolo_del_messaggio("Prova")
# print(email.get_all())

'''Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:


Percorso: nomePercorso/document.txt
Contenuto: Questo e' il contenuto del file.'''

class File(Documento):
    def __init__(self,testo: str, nome_percorso: str):
        super().__init__(testo)
        self.nome_percorso = nome_percorso
    def getTesto(self) -> str:
        return super().getText()
    
    def leggiTestodaFile(self):
        with open(self.nome_percorso,"r") as contenuto:
            self.testo = contenuto.read()
    def getText(self):
        return f"Percorso: {self.nome_percorso}\n Contenuto: {self.getTesto()}"
    

# file1 = File("caio e semptiono",r"C:\Users\Majinbu\Vscodeprojects\Esercizi\Lezione24\document.txt")
# file1.leggiTestodaFile()
# print(file1.getText())




n1 = 100
n2 = 200
count = 0
matrice = []

for i in range(n1):
    raw = []
    for j in range(n2):
        count += 1
        raw.append(count)
    matrice.append(raw)

print(count)
matrice[i][j]

count = 0
i = 0
j = 0
while i < n1:
    while j < n2:
        count += 1
        j += 1
    i += 1
    j = 0

'''
import random
random.seed(0)

lst = [random.random(0, 100000) for _ in range(n2)]
print(lst) 
max_val = 0
for val in lst:
    if val > max_val:
        max_val = val

print(max_val)
#lista causali di interi tra 0 a 100000

max_val = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if i == j: continue
        if lst[i] == lst[j]:
            print("c'e un duplicato")
    
print(max_val)
'''
#vedere se c'è un duplicato su una lista

ciao = {"piip":"bibbio"}

print(ciao[1])







### Test tramite codice driver:
'''Creazione degli oggetti:

    Email: Viene creato un oggetto Email con mittente, destinatario, oggetto e corpo del messaggio.
    File: Viene creato un oggetto File specificando il percorso di un file esistente.

Prova dei metodi:

    Stampa del testo dell'email: Viene stampato il testo del messaggio dell'email utilizzando il metodo getText().
    Stampa del testo del file: Viene stampato il contenuto del file utilizzando il metodo getText().

Scrittura del contenuto dell'email su un file:

    Scrittura su file: Il contenuto dell'email viene scritto su un nuovo file chiamato email1.txt utilizzando il metodo writeToFile().

Verifica della presenza di parole chiave:

    Email: Utilizzo del metodo isInText() per verificare se la parola 'incontrarci' è presente nel testo dell'email. Il risultato atteso è True.
    File: Utilizzo del metodo isInText() per verificare se la parola 'percorso' è presente nel testo del file. Il risultato atteso è False.

### Test con UnitTest

Utilizzando il modulo unittest, definire i seguenti test per le classi Documento, Email e File.
 
I test devono includere:

    Verifica dei metodi getText() e setText() nella classe Documento.
    Verifica del metodo isInText() nella classe Documento.
    Verifica del metodo getText() nella classe Email.
    Verifica del metodo writeToFile() nella classe Email.
    Verifica del metodo isInText() nella classe Email.
    Verifica del metodo getText() nella classe File.
    Verifica del metodo isInText() nella classe File.'''
