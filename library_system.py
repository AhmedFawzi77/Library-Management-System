class Book:
    def __init__(self, name, book_id, copies):
        self.name = name
        self.book_id = book_id
        self.copies = copies

    def __repr__(self):
        return f"Book(Name: {self.name}, ID: {self.book_id}, Copies: {self.copies})"

class Admin:
    def __init__(self, name="Library Admin"):
        self.name = name

    def add_book(self, library):
        name = input("Enter book name: ")
        book_id = input("Enter book ID: ")
        copies = int(input("Enter number of copies: "))
        new_book = Book(name, book_id, copies)
        library.books.append(new_book)
        print(f"Admin {self.name} added book: {name} successfully.")
        library.list_available_books()

    def update_book(self, library):
        book_id = input("Enter book ID to update: ")
        book = next((b for b in library.books if b.book_id == book_id), None)
        if book:
            new_name = input("Enter new book name (leave blank to keep the current name): ")
            new_copies = input("Enter new number of copies (leave blank to keep the current count): ")
            if new_name:
                book.name = new_name
            if new_copies:
                book.copies = int(new_copies)
            print(f"Admin {self.name} updated book ID {book_id} successfully.")
            library.list_available_books()
        else:
            print(f"Book with ID {book_id} not found.")

    def delete_book(self, library):
        book_id = input("Enter book ID to delete: ")
        book = next((b for b in library.books if b.book_id == book_id), None)
        if book:
            library.books.remove(book)
            print(f"Admin {self.name} deleted book ID {book_id} successfully.")
            library.list_available_books()
        else:
            print(f"Book with ID {book_id} not found.")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.borrowed_books = []

    def search_book(self, library, search_term):
        """Search for a book by name or ID."""
        for book in library.books:
            if book.book_id == search_term or book.name.lower() == search_term.lower():
                return book
        return None

    def borrow_book(self, library):
        search_term = input("Enter book name or ID to borrow: ")
        book = self.search_book(library, search_term)
        if book and book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book)
            print(f"{self.username} borrowed {book.name}.")
            library.list_available_books()
        elif book:
            print(f"Sorry, {book.name} is out of stock.")
        else:
            print(f"Book '{search_term}' not found.")

    def buy_book(self, library):
        search_term = input("Enter book name or ID to buy: ")
        book = self.search_book(library, search_term)
        if book and book.copies > 0:
            book.copies -= 1
            print(f"{self.username} bought {book.name}.")
            library.list_available_books()
        elif book:
            print(f"Sorry, {book.name} is out of stock.")
        else:
            print(f"Book '{search_term}' not found.")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []
        self.admins = []

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if any(u.username == username for u in self.users):
            print(f"User {username} already exists.")
        else:
            new_user = User(username, password)
            self.users.append(new_user)
            print(f"User {username} signed up successfully.")

    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = next((u for u in self.users if u.username == username and u.password == password), None)
        if user:
            print(f"User {username} logged in successfully.")
            return user
        else:
            print("Invalid username or password.")
            return None

    def add_admin(self, admin):
        self.admins.append(admin)
        print(f"Admin {admin.name} added to library.")

    def list_available_books(self):
        print("\nAvailable Books:")
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(f"Book: {book.name}, ID: {book.book_id}, Copies: {book.copies}")
        print("-" * 30)

def main_menu(library):
    while True:
        print("\nMain Menu:")
        print("1. Admin Operations")
        print("2. User Operations")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            admin_operations(library)
        elif choice == "2":
            user_operations(library)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

def admin_operations(library):
    admin = library.admins[0]  
    
    while True:
        print("\nAdmin Operations:")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            admin.add_book(library)
        elif choice == "2":
            admin.update_book(library)
        elif choice == "3":
            admin.delete_book(library)
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option, please try again.")

def user_operations(library):
    while True:
        print("\nUser Options:")
        print("1. Register User")
        print("2. Login")
        print("3. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            library.register_user()
        elif choice == "2":
            user = library.login_user()
            if user:
                logged_in_user_operations(library, user)
        elif choice == "3":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option, please try again.")

def logged_in_user_operations(library, user):
    while True:
        print("\nUser Operations (Logged in):")
        print(f"Logged in as {user.username}")
        print("1. Borrow Book")
        print("2. Buy Book")
        print("3. Logout")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            user.borrow_book(library)
        elif choice == "2":
            user.buy_book(library)
        elif choice == "3":
            print(f"Logging out {user.username}...")
            break
        else:
            print("Invalid option, please try again.")

library = Library("AHMED_FAWZI Library")
admin = Admin()  
library.add_admin(admin)

main_menu(library)