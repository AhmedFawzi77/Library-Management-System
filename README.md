

# **Library Management System**

## **Project Description**
The **Library Management System** is a Python-based console application designed to manage books in a library. It provides functionalities for both **admins** and **users**. Admins can manage the library's collection of books, including adding new books, updating book details, and deleting old books. Users can register, log in, search for books, borrow them, and even purchase them if they wish. This project is built around basic **object-oriented principles**.

### **System Overview**
1. **Admin**: Manages books by adding, updating, and deleting them. Can also view the list of available books.
2. **User**: A regular user can search for books, borrow them, and purchase them. Each user can borrow multiple books at a time.
3. **Library**: Holds the list of books, users, and admins. It manages operations like registering users, logging them in, listing books, and managing book collections.

## **Features**
### Admin Features:
- **Add Books**: Admins can add books to the library with details such as the book's name, ID, and available copies.
- **Update Books**: Admins can modify existing books' details, including the number of copies and the book's name.
- **Delete Books**: Admins can delete a book from the library using its ID.
  
### User Features:
- **Register**: Users can register by providing a username and password.
- **Login**: Registered users can log into the system.
- **Search Books**: Users can search for books either by name or ID.
- **Borrow Books**: Users can borrow books if they are available. The number of available copies is decreased after borrowing.
- **Buy Books**: Users can purchase books that are available in the library. The number of copies is decreased after purchase.

### Library Features:
- **List Available Books**: Display all the books in the library along with their details (name, ID, and copies).
- **Book Availability**: For each book, show whether it is available for borrowing or purchasing.

## **Usage**

### Start the Program:
When the program runs, you'll be presented with a menu to choose between **Admin** or **User** operations.

### Admin Operations:
Admin can perform tasks like adding, updating, or deleting books.

### User Operations:
Users can register, log in, borrow, and buy books from the library.

### Logging In:
Once logged in, users can borrow books from the library or buy books based on availability.

---

## **Example Workflow**

1. **Start the Program**:  
   After starting the program, select option 1 for **Admin Operations**.
   
2. **Add a Book**:  
   Admin adds a new book with details such as:  
   - Book Name: "Python 101"  
   - Book ID: "101"  
   - Copies: 5  
   Admin selects the option to add the book, and the system confirms the addition.

3. **Select 2 for User Operations**:  
   The admin or user selects option 2 for **User Operations**.  

4. **Register a User**:  
   A user enters their desired username and password to register.

5. **Login**:  
   The user logs in with the registered credentials. If successful, the user is authenticated.

6. **Borrow a Book**:  
   The logged-in user searches for a book and borrows it. The system updates the book’s available copies accordingly.

7. **Buy a Book**:  
   The user purchases a book. The system decreases the available copies of the book.

## **Key Classes**
1. **Book**  
   This class is responsible for representing a book in the library. Each book has:
   - `name`: The name of the book.
   - `book_id`: A unique identifier for the book.
   - `copies`: The number of copies available for borrowing or purchasing.
   The class has methods to display book information when required.

2. **Admin**  
   The Admin class represents the administrator of the library. Admins have the following functionalities:
   - Add books to the library.
   - Update book details like name or available copies.
   - Delete books that are no longer needed.

3. **User**  
   The User class represents a user of the library. Each user has:
   - `username`: The unique username for each user.
   - `password`: A password for user authentication.
   - `borrowed_books`: A list that keeps track of the books a user has borrowed.
   Users can:
   - Register and log in to the system.
   - Search, borrow, and buy books.

4. **Library**  
   The Library class is the core of the system and manages:
   - The list of all books in the library.
   - The list of registered users.
   - The list of admins.
   It provides methods to add books, list available books, and manage users.

## **Concepts Applied**
1. **Object-Oriented Programming (OOP):**
   - **Classes and Objects**: Classes are used to model the real-world entities in the system, such as books, users, and admins. These classes define the properties and behaviors of each entity. For example, the `Book` class defines the attributes of a book and provides a method to display book information.
   - **Encapsulation**: Encapsulation is the concept of bundling the data (attributes) and methods that operate on the data (functions) within a class. In this project, each entity (like books, users, and admins) is encapsulated within a class. For example, the `User` class handles user-related functions such as borrowing and purchasing books.
   - **Abstraction**: Abstraction is the process of hiding the complex implementation details and providing a simple interface to the user. In this system, methods such as `add_book`, `borrow_book`, or `buy_book` hide the internal implementation and present a simple interface to interact with the system.

2. **Search Algorithm:**
   - The system uses a **linear search** algorithm to search for books by their name or ID. This search method iterates through the list of books and compares each book's name or ID with the user's search input. If a match is found, the book is returned to the user.

3. **Input/Output Management:**
   - The system manages interaction with the user via the console using `input` and `print`. For instance, when an admin adds a book, they are prompted to provide the book's details, and the system outputs a confirmation message.
   - Similarly, users can search for books and borrow or purchase them, with the system printing relevant messages to indicate success or failure.

4. **List Management:**
   - The system stores books, users, and admins in lists. The `Library` class manages these lists. Books are added, updated, or deleted from the `books` list, and users are registered and logged in through the `users` list.

5. **Error Handling:**
   - The system includes basic error handling to guide users through the application and provide informative messages. For example, if a user tries to borrow a book that is out of stock, the system informs them that the book is not available.
