import re
import csv
import os
from library import Book, User, Library

def validate_isbn(isbn):
    return bool(re.match(r"^\d{3}-\d{10}$", isbn))

def validate_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email))

def load_books(file_path):
    try:
        with open(file_path, "r") as file:
            return [{"isbn": row[0], "title": row[1], "author": row[2]} for row in csv.reader(file)][1:]
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []

def save_books(books, file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["isbn", "title", "author"])
        for book in books:
            writer.writerow([book.isbn, book.title, book.author])

def write_transaction_log(user_id, isbn, action):
    with open("data/transactions.txt", "a") as file:
        file.write(f"{user_id}, {isbn}, {action}\n")

library = Library()

os.makedirs("data", exist_ok=True)
books_file_path = "data/books.csv"

if not os.path.exists(books_file_path):
    save_books([], books_file_path)
    print(f"File {books_file_path} created.")

for book_data in load_books(books_file_path):
    library.add_book(Book(book_data["isbn"], book_data["title"], book_data["author"]))

def main_menu():
    actions = {
        "1": add_book,
        "2": add_user,
        "3": issue_book,
        "4": return_book,
        "5": list_books,
        "6": list_users,
        "7": exit_program
    }

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add User")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Users")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please try again.")

def add_book():
    isbn = input("Enter ISBN (format: XXX-XXXXXXXXXX): ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format!")
        return

    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    library.add_book(Book(isbn, title, author))
    save_books(library.books, books_file_path)
    print(f"Book '{title}' added")

def add_user():
    user_id = input("Enter user ID: ")
    name = input("Enter user name: ")
    email = input("Enter user email: ")

    if not validate_email(email):
        print("Invalid email format!")
        return

    library.add_user(User(user_id, name, email))
    print(f"User '{name}' with email '{email}' added ")

def issue_book():
    user_id = input("Enter your user ID: ")
    isbn = input("Enter the book ISBN: ")
    result = library.issue_book(isbn, user_id)
    write_transaction_log(user_id, isbn, "Issued")
    print(result)

def return_book():
    isbn = input("Enter the book ISBN: ")
    write_transaction_log("", isbn, "Returned")
    print(library.return_book(isbn))

def list_books():
    books = library.list_books()
    if books:
        print("\nBooks in Library:")
        print("\n".join(map(str, books)))
    else:
        print("There is no availability of this book in the library!")

def list_users():
    users = library.list_users()
    if users:
        print("\nRegistered Users:")
        print("\n".join(map(str, users)))
    else:
        print("No users registered.")

def exit_program():
    print("Exiting")
    exit()

if __name__ == "__main__":
    main_menu()