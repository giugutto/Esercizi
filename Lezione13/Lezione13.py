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




class Member:
    def __init__(self, member_id: str,name: str, borrowed_book: list[Book] = []) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_book: list = borrowed_book


    def borrow_book(self, book: Book):
        self.borrowed_book.append(book)
        
            
    def return_book(self, book:Book):
        self.borrowed_book.remove(book)


class Library:
    def __init__(self, books: dict[str, Book] = {}, members:dict[str, Member] = {}) -> None:
        self.books = books
        self.members = members


    def add_book(self, book_id: str, title: str, author: str):
        book = Book(book_id, title, author)
        self.books[book_id] = book
    def register_member(self, member_id:str, name: str):
        member = Member(member_id, name)
        self.members[member_id] = member
    def borrow_book(self, member_id: str, book_id: str):
        if book_id in self.books and not self.books[book_id].is_borrowed:
            self.books[book_id].borrow()
            self.members[member_id].borrow_book(self.books[book_id])
        else:
            raise ValueError()
    def return_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)
        else:
            raise ValueError()
        
    def get_borrowed_books(self, member_id) -> list[Book]: # restituisce la lista dei libri presi in prestito dal membro.
        print(self.members[member_id].borrowed_book)
    





