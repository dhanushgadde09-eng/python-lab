# Library Management System

books = []

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    books.append({"id": book_id, "title": title, "author": author, "issued": False})
    print("Book added successfully.")

def view_books():
    if not books:
        print("No books in the library.")
    else:
        for book in books:
            status = "Issued" if book["issued"] else "Available"
            print(book["id"], "|", book["title"], "|", book["author"], "|", status)

def issue_book():
    book_id = input("Enter book ID to issue: ")
    for book in books:
        if book["id"] == book_id:
            if not book["issued"]:
                book["issued"] = True
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            return
    print("Book not found.")

def return_book():
    book_id = input("Enter book ID to return: ")
    for book in books:
        if book["id"] == book_id:
            if book["issued"]:
                book["issued"] = False
                print("Book returned successfully.")
            else:
                print("This book was not issued.")
            return
    print("Book not found.")

while True:
    print("\n--- Library Management ---")
    print("1. Add book")
    print("2. View books")
    print("3. Issue book")
    print("4. Return book")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Exiting library system.")
        break
    else:
        print("Invalid choice.")

output
--- Library Management ---
1. Add book
2. View books
3. Issue book
4. Return book
5. Exit
Enter choice: 2
567 | agriculture | watson | Available

--- Library Management ---
1. Add book
2. View books
3. Issue book
4. Return book
5. Exit
Enter choice: 3
Enter book ID to issue: 567
Book issued successfully.

--- Library Management ---
1. Add book
2. View books
3. Issue book
4. Return book
5. Exit
Enter choice: 4
Enter book ID to return: 567
Book returned successfully.

--- Library Management ---
1. Add book
2. View books
3. Issue book
4. Return book
5. Exit
Enter choice: 5
Exiting library system.
