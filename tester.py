import pytest
from main import validate_isbn, load_books, save_books, write_transaction_log
from library import Book, User, Library

def test_validate_isbn():
    assert validate_isbn("123-1234567890") == True
    assert validate_isbn("123-12345") == False
    assert validate_isbn("abc-1234567890") == False
    assert validate_isbn("1234567890") == False

def test_load_books():
    books = [{"isbn": "123-1234567890", "title": "Test Book", "author": "Test Author"}]
    assert len(books) == 1
    assert books[0]["isbn"] == "123-1234567890"
def test_add_book():
    library = Library()
    book = Book("123-1234567890", "Test Book", "Test Author")
    library.add_book(book)
    assert len(Library.books) == 1
    assert Library.books[0].isbn == "123-1234567890"

def test_add_user():
    Library = Library()
    user = User("user001", "Test User", "testuser@example.com")
    Library.add_user(user)
    assert len(Library.users) == 1
    assert Library.users[0].email == "testuser@example.com"

def test_write_transaction_log():
    write_transaction_log("user123", "123-1234567890", "Issued")
    with open("data/transactions.txt", "r") as file:
        logs = file.readlines()
    assert len(logs) > 0
    assert "user123" in logs[-1]
    assert "123-1234567890" in logs[-1]