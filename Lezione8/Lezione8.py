#Lezione 8
#EREDITARIETÀ E POLISMOSFIRMO

class Operazione:
    def __init__(self, operando) -> None:
        self.operando = operando

class OperazioneBinaria(Operazione):
    def __init__(self, operando, arg1, arg2) -> None:
        super().__init__(operando)
        self.arg1 = arg1
        self.arg2 = arg2
    #stiamo aggiungendo metodi alla sottoclasse operazionebinaria che prende l'attributo operando della superclasse
    def set_arg1(self,arg1): #setter
        self.arg1 = arg1

    def set_arg2(self, arg2): #setter
        self.arg2 = arg2

    def get_arg1(self): #getter
        return self.arg1
    
    def get_arg2(self): #getter
        return self.arg2
        
    def somma(self):
        return self.arg1 + self.arg2
    def esegui_operazione(self):
        if self.operando == '+':
            return self.somma()
        
    #il metodo statico prende degli input e eresituisce un output ma non accede agli attributi della classe
    #il metodo statico non accede allo stato dell'oggetto non avendo il self
    @staticmethod
    def static_sum(arg1: int, arg2:int):
        return arg1 + arg2
    def esegui_operazione(self):
        if self.operando == '+':
            return OperazioneBinaria.static_sum(self.arg1, self.arg2)
        
op = OperazioneBinaria('+', 5, 23)
print(op.esegui_operazione())

