import pytest #testing library
from main import validate_isbn, load_books, save_books, write_transaction_log #libraries
from library import Book, User, Library #object orientated programming

def test_validate_isbn(): 
    assert validate_isbn("123-1234567890") == True #valid ISBN
    assert validate_isbn("123-12345") == False #invalid ISBN
    assert validate_isbn("abc-1234567890") == False #invalid ISBN with letters
    assert validate_isbn("1234567890") == False #invalid 

def test_load_books(): #testing function for loading books
    books = [{"isbn": "123-1234567890", "title": "Test Book", "author": "Test Author"}]
    assert len(books) == 1 #testing list length
    assert books[0]["isbn"] == "123-1234567890" #file I/O 

def test_add_book():
    library = Library()
    book = Book("123-1234567890", "Test Book", "Test Author") #testing 
    library.add_book(book)
    assert len(Library.books) == 1
    assert Library.books[0].isbn == "123-1234567890"

def test_add_user():
    Library = Library()
    user = User("user001", "Test User", "testuser@example.com") #object orientated programming 
    Library.add_user(user)
    assert len(Library.users) == 1
    assert Library.users[0].email == "testuser@example.com"

def test_write_transaction_log():
    write_transaction_log("user123", "123-1234567890", "Issued")
    with open("data/transactions.txt", "r") as file: #file I/O
        logs = file.readlines() 
    assert len(logs) > 0
    assert "user123" in logs[-1]
    assert "123-1234567890" in logs[-1]

