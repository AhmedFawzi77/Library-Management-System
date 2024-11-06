
# Library Management System

## Project Description
This **Library Management System** is a Python-based application that allows users to interact with a library by performing various operations such as searching, borrowing, and purchasing books. Admins can manage books, including adding, updating, and deleting them. The system supports user registration, login, and session management.

## Features
- **Admin Operations:**
  - Add new books to the library.
  - Update book details (name, number of copies).
  - Delete books from the library.
  
- **User Operations:**
  - Register a new user.
  - Login to the system.
  - Search for books by name or ID.
  - Borrow books if they are available.
  - Buy books if they are available.

- **Library Operations:**
  - List all available books with their details (name, ID, and number of copies).
  - Display books' availability status.

## Key Classes
1. **Book**  
   This class defines a book object with attributes such as name, book ID, and the number of copies available.
   
2. **Admin**  
   Represents an admin user with operations like adding, updating, and deleting books in the library.
   
3. **User**  
   Represents a library user with operations to search for, borrow, and buy books.

4. **Library**  
   The core class for managing users, books, and admins. It allows operations like user registration, book listing, and adding/removing books.

## Concepts Applied
1. **Object-Oriented Programming (OOP):**
   - **Classes and Objects:** The core entities such as `Book`, `User`, `Admin`, and `Library` are implemented as classes. Instances (objects) of these classes are used to perform various operations in the system.
   - **Encapsulation:** The details of each entity (e.g., book details such as name, ID, and number of copies) are encapsulated within their respective classes. The operations for adding, updating, and deleting books are also encapsulated within the `Admin` class, and the operations for borrowing and buying books are encapsulated within the `User` class.
   - **Abstraction:** Complex operations like adding a book, borrowing a book, or searching for a book are abstracted into methods in the respective classes, making the system easier to use and extend.

2. **Search Algorithm:**
   - A simple linear search algorithm is used to find books by their name or ID within the library.

3. **Input/Output Management:**
   - The system interacts with the user through input and output operations, such as asking the user for book details (name, ID, number of copies) and managing user login credentials.

4. **List Management:**
   - The library manages its books and users using lists. Each list is updated dynamically based on user actions (e.g., adding/removing books, registering users).

5. **Error Handling:**
   - Basic error handling is implemented to ensure that users are informed when they attempt to interact with non-existent books or provide incorrect login credentials.
