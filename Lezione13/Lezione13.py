# Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se 
# l'albero è simmetrico; False altrimenti.

# La lista di interi è formata così:

#     L'elemento in posizione 0 corrisponde alla radice
#     Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
#     Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
#     Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, 
# significa che il nodo che corrisponde a quell'indice è una foglia.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool:
    if tree[1] != tree[2]:
        False

    else:
        if tree[3] == tree[6] and tree[4] == tree[5]:
            return True
        else:
            return False


print(symmetric([1,2,2,3,4,4,3]))

# Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

#     Classe Book:
#         Attributi:
#             book_id: str - Identificatore di un libro.
#             title: str - titolo del libro.
#             author: str - autore del libro
#             is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
#         Metodi:
#             borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
#             return_book()- Contrassegna il libro come restituito.

#     Classe Member:
#         Attributi:
#             member_id: str - identificativo del membro.
#             name: str - il nome del membro.
#             borrowed_books: list[Book] - lista dei libri presi in prestito.
#         Metodi:
#             borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
#             return_book(book): rimuove il libro dalla lista borrowed_books.

#     Classe Library:
#         Attributi:
#             books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
#             members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
#         Metodi:
#             add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
#             register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
#             borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
#             return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
#             get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.




class Book:
    def __init__(self, book_id: str, title:str, author: str, is_borrowed: bool = False) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
    
    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False

    def __str__(self) -> str:
        return self.title




class Member:
    def __init__(self, member_id: str,name: str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_book: list = []


    def borrow_book(self, book: Book):
        if book.is_borrowed == False:
            self.borrowed_book.append(book)
            book.borrow()
       
        
            
    def return_book(self, book:Book):
        self.borrowed_book.remove(book)
        book.return_book()



class Library:
    def __init__(self) -> None:
        self.books = {}
        self.members = {}


    def add_book(self, book_id: str, title: str, author: str):
        book = Book(book_id, title, author)
        self.books[book_id] = book
    def register_member(self, member_id:str, name: str):
        member = Member(member_id, name)
        self.members[member_id] = member
    def borrow_book(self, member_id: str, book_id: str):
        if book_id in self.books:
            if not self.books[book_id].is_borrowed:
                if member_id in self.members:
                    self.members[member_id].borrow_book(self.books[book_id])
                else: 
                    raise ValueError('Member not found')
            else:
                raise ValueError("Book is already borrowed")
        else:
            raise ValueError('Book not found')
    def return_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            if book.is_borrowed:
                member.return_book(book)
            else:
                raise ValueError("Book not borrowed by this member")
        
    def get_borrowed_books(self, member_id) -> list[Book]: # restituisce la lista dei libri presi in prestito dal membro.
        return [i.__str__() for i in self.members[member_id].borrowed_book]


library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")


 # Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")


# Edge case - trying to borrow a book by a non-existent member
try:
    library.borrow_book("M004", "B001")
except ValueError as e:
    print(e)

 	
ESERCIZIO 3
# Data una stringa s e una lista di stringhe wordDict, 
# restituisce True se s può essere segmentato in una sequenza separata da spazi di una o più parole del dizionario;
# False altrimenti.
# Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.
# print(word_break("leetcode",["leet","code"]))
# True
# print(word_break("applepenapple", ["apple","pen"]))
# True
# print(word_break("catsandog",["cats","dog","sand","and","cat"]))
# False
def world_break(stringa: str, lista: list):
    

ESERCIZIO 4
# Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.

# For example:
# Test 	Result

# head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
# print(reverse_list(head))

	

# [5, 4, 3, 2, 1]

# head = ListNode(val=1, next=ListNode(val=2))
# print(reverse_list(head))

ESERCIZIO 6
# Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

#     Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
#     Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
#     Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.

# Nota:

#     Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
#     Solo le celle riempite devono essere convalidate secondo le regole menzionate.
ESERCIZIO 7
# Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

# Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.

# For example:
# Test 	Result

# print(anagram("anagram","nagaram"))

	

# True
ESERCIZIO BANCA
# Progettare un semplice sistema bancario con i seguenti requisiti:

#     Classe del Account:
#         Attributi:
#             account_id: str - identificatore univoco per l'account.
#             balance: float - il saldo attuale del conto.
#         Metodi:
#             deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#             get_balance(): restituisce il saldo corrente del conto.
#     Classe Bank:
#         Attributi:
#             accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#         Metodi:
#             create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#             deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#             get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

# For example:
# Test 	Result

# bank = Bank()
# account1 = bank.create_account("123")
# print(account1.get_balance())

	

# 0

# bank = Bank()
# account1 = bank.create_account("123")
# bank.deposit("123",100)
# print(bank.get_balance("123"))

	

# 100

# bank = Bank()
# account2 = bank.create_account("456")
# bank.deposit("456",200)
# print(bank.get_balance("456"))

	

# 200