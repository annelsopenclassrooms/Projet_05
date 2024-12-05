class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return (f"title={self.title}, "
                f"author={self.author}, year={self.year}")


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []
    # Ajouter les méthodes ici

    # Ajoute un livre à la bibliothèque
    def add_book(self, book):
        self.books.append(book)

    # Supprime un livre de la bibliothèque en utilisant le titre du livre comme argument.
    def remove_book(self, book_title):
        result = next((book for book in self.books if book.title == book_title), None)
        self.books.remove(result)

    # Emprunte un livre de la bibliothèque en utilisant le titre du livre comme argument.
    # Le livre doit être retiré de la liste des livres disponibles et ajouté dans la liste des livres empruntés.
    def borrow_book(self, book_title):
        result = next((book for book in self.books if book.title == book_title), None)
        self.borrow_books.append(result)
        self.books.remove(result)

    # Rend un livre emprunté à la bibliothèque en utilisant le titre du livre comme argument.
    # Le livre doit être retiré de la liste des livres empruntés et ajouté dans la liste des livres disponibles.
    def return_book(self, book_title):
        result = next((book for book in self.borrow_books if book.title == book_title), None)
        self.borrow_books.remove(result)
        self.books.append(result)

    # Renvoie une liste contenant les titres des livres disponibles dans la bibliothèque.
    def available_books(self):
        print(f"Livres disponibles: ")
        for book in self.books:
            print(book)

    # Renvoie une liste contenant les titres des livres empruntés de la bibliothèque.
    def borrowed_books(self):
        print(f"Livres empruntés: ")
        for book in self.borrow_books:
            print(book)


library = Library()

book1 = Book("Hyperion", "Simmons", "1989")
book2 = Book("Endymion", "Simmons", "1991")

library.add_book(book1)
library.add_book(book2)
library.add_book(Book("Carrie", "King", "1974"))

print(library.books)

#library.remove_book("Hyperion")

library.borrow_book("Hyperion")


library.available_books()
library.borrowed_books()