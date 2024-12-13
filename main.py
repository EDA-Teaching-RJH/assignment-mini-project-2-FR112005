from models import Book, user, library
from utilities import validate_isbn, validate_email, load_books, save_books, write_transaction_log

library = library()

for book_data in load_books("data/books.csv"):
    library.add_book(Book(book_data["isbn"]. book_data["title"], book_data["author"]))

def main_menu():
    while True: 
        print("\nLibrary Management system")
        print("1. Add Book Title")
        print("2. Add Your User")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. List all the books")
        print("6. List all users")
        print("7. Exit")

        choice = input("Enter your choices: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            add_user()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            list_book()
        elif choice == "6":
            list_users()
        elif choice == "7":
            print("Exiting the system now. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
def add_book(): 
    isbn = input("Enter ISBN (format: XXX-XXXXXXXXXX): ")
    if not validate_isbn(isbn): 
        print("Invalid ISBN format!")
        return 
    
    title = input("Enter the book title:")
    author = input("Enter book author:") 

    book = Book(isbn, title, author)
    library.add_book(book)
    save_books(library.books, "data/books.csv")
    print(f"book '{title}' added successfully!")

def add_user(): 
    user_id = input("Enter user ID:")
    name = input("Enter user name:")
    email = input("Enter user email:") 
    
    if not validate_email(email): 
        print("This is an invalid email format")
        return 
    
    user = user(user_id, name, email)
    library.add_user(user)
    print(f"User '{name}' added successfully!")

def issue_book(): 
    user_id = input("Enter your user ID please") 
    isbn = input("Enter the book ISBN: ")
    result = library.issue_book(isbn, user_id)
    write_transaction_log(user_id, isbn, "Issued")
    print(result)

def return_book():
    isbn = input("Enter the book ISBN:")
    write_transaction_log("", isbn, "returned")

def list_books():
    books = library.list_books()
    if books:
        print("\nBooks in Library:") 
        for book in books:
            print(book)
    else:
        print("There is no availability of this book in the library!")

def list_users():
    users = library.list_users()
    if users:
        print("\nRegistered Users:")
        for user in users:
            print(user)
    else:
        print("No users registered")

if __name__ == "__main__":
    main_menu() 
