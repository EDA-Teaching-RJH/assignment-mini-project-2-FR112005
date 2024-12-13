class Book: #book is the object #library 
    def __init__(self, isbn, title, author): 
        self.isbn = isbn #ISBN of book #OOP: Behaviour 
        self.title = title #title of book #OOP: Behaviour 
        self.author = author #author of book #OOP: Behaviour 
        self.is_available = True #shows if book is available 

    def __str__(self): #returns a string for printing
        status = "Availble" if self.is_available else "issued" #OOP: Attributes  
        return f"{self.isbn} | {self.title} by {self.author} - {status}" #OOP: Behaviour

class user: #user object in the library 
    def __init__(self, user_id, name, email): #returns string representation 
        self.user = user_id #asking for ID
        self.name = name #asking for name
        self.email = email #asking for email

    def __str__(self): #returns a string of the user's info
        return f"{self.user_id} | {self.name} ({self.email})"

class library: #represents library, managing books and users
    def __init__(self): 
        self.books = [] #list of books in library
        self.users = [] #list of the users registered
    
    def add_book(self, book): #adds new book to collection
        self.books.append(book)
    
    def add_user(self, user): #registers new user for library
        self.users.append(user)

    def issue_book(self, isbn, user_id): #issues the book to user
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False #book is issued
                return f"Book '{book.title}' issued to User ID: {user_id}"
            return "Book is not available or ISBN is invalid"

    def return_book(self, isbn): #shows book is returned 
        for book in self.books: 
            if book.isbn == isbn and not book.is_available: 
                book.is_available = True #shows book as available 
                return f"Book '{book.title}' has been returned." 
        return "Book is not issued or ISBN is invalid." 
    
    def list_books(self): #shows all books in library
        return [str(book) for book in self.books]
    
    def list_users(self): #shows all users in library 
        return [str(user) for user in self.users]
    
    
    