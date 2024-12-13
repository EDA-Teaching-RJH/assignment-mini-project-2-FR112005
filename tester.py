import re
import csv 

def validate_isbn(isbn): 
    pattern = r"^\d{3}-\d{10}$"
    return bool(re.match(pattern, isbn))
    
def validate_email(email): 
    pattern = r"^[w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def load_books(file_path):
    books = []
    try:
        with open(file_path, "r") as file: 
            reader = csv.reader(file)
            for row in reader:
                books.append({"isbn": row[0], "title": row[1], "author": row[2]})
    except FileNotFoundError:
        pass
    return books

def save_books(books, file_path):
    with open(file_path, "w", newlines="") as file: 
        writer = csv.writer(file)
        for book in books: 
            writer.writerow([book.isbn, book.title. book.author])

def write_transaction_log(user_id, isbn, action):
    with open("data/transactions.txt", "a") as file: 
        file.write(f"{user_id}, {isbn}, {action}\n")