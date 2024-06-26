# Esercizio 1

# Crea un context manager usando una classe
# Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.
# Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__
# Esempio di funzionamento:
# Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.
# with FileManager('example.txt', 'w') as f:
#     f.write('Hello, world!')

from contextlib import contextmanager

class Filemanager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            tb.print_exception(exc_type, exc_value, tb)
        self.file.close()
        return False
    

        
with Filemanager('example.txt', 'w') as f:
    f.write('Hello, World!')

with open('example.txt', 'r') as f:
    print(f.read())

def filemanager(func):
    def wrapper(*args):
        print("Apertura File")
        func(*args)
        print("File chiuso")
    return wrapper

@filemanager
def fileopen(filename, mode):
    with Filemanager(filename, mode):
        f.write("ciao monso!")
        f.close()







# Esercizio 2

# Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

# with Timer():

#     time.sleep(1)

# time elapsed: 1.00000

# in questo esempio il tempo passato non sarà mai uguale a 1

