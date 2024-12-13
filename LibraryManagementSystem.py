import re 
import csv 

class Book: 
    def __init__(self, isbn, title, author):
        self.isbn = isbn 
        self.title = title 
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Availble" if self.is_available else "issued"
        return f"{self.isbn} | {self.title} by {self.author} - {status}"

class user:
    def __init__(self, user_id, name, email):
        self.user = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.user_id} | {self.name} ({self.email})"

class library: 
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book): 
        self.books.append(book)
    
    def add_user(self, user):
        self.users.append(user)

    def issue_book(self, isbn, user_id):
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False
                return f"Book '{book.title}' issued to User ID: {user_id}"
            return "Book is not available or ISBN is invalid"

    def return_book(self, isbn):
        for book in self.books: 
            if book.isbn == isbn and not book.is_available: 
                book.is_available = True 
                return f"Book '{book.title}' has been returned." 
        return "Book is not issued or ISBN is invalid." 
    
    def list_books(self):
        return [str(book) for book in self.books]
    
    def list_users(self):
        return [str(user) for user in self.users]
    
    
    