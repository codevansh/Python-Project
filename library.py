library_users = {
    "user1": {"password": "11192081", "borrowed_books": []},
    "user2": {"password": "22114198", "borrowed_books": []},
    "user3": {"password": "1358201", "borrowed_books": []}
}

library_books = {
    "OS": "Available",
    "DBMS": "Available",
    "MATHS": "Available",
    "MP": "Available",
    "AOA": "Available",
}

def show_borrowed_books(borrowed_books):
    if borrowed_books:
        print("Your Borrowed Books:")
        for book in borrowed_books:
            print(f"- {book}")
    else:
        print("You have not borrowed any books yet.")

def borrow_book(user_name):
    print("\n Available Books:")
    available_books = [book for book, status in library_books.items() if status == "Available"]
    
    if not available_books:
        print("No books are available at the moment.")
        return
    for book in available_books:
        print(f"- {book}")
        
    book_choice = input("Enter the name of the book you want to borrow: ")
    if book_choice in library_books and library_books[book_choice] == "Available":
        library_users[user_name]["borrowed_books"].append(book_choice)
        library_books[book_choice] = "Borrowed"
        print(f"You have successfully borrowed '{book_choice}'.")
    else:
        print("Invalid choice or the book is already borrowed.")

def return_book(user_name):
    borrowed_books = library_users[user_name]["borrowed_books"]
    if not borrowed_books:
        print("You have no borrowed books to return.")
        return
    
    print("\nYour Borrowed Books:")
    for book in borrowed_books:
        print(f"- {book}")
        
    book_choice = input("Enter the name of the book you want to return: ")
    if book_choice in borrowed_books:
        library_users[user_name]["borrowed_books"].remove(book_choice)
        library_books[book_choice] = "Available"
        print(f"You have successfully returned '{book_choice}'.")
    else:
        print("You did not borrow this book.")

def authenticate_user(user_name, password):
    if library_users[user_name]["password"] == password:
        print("Login Successful")
        return True
    else:
        print("Incorrect Password. Access Denied.")
        return False

def user_menu(user_name):
    is_running = True
    while is_running:
        print("\n1. Show Borrowed Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_borrowed_books(library_users[user_name]["borrowed_books"])
        elif choice == '2':
            borrow_book(user_name)
        elif choice == '3':
            return_book(user_name)
        elif choice == '4':
            return False
        else:
            print("Enter a valid choice.")
    return True

def main():
    code_running = True
    while code_running:
        print("\n*** Library Management System ***")
        print("1. User-1")
        print("2. User-2")
        print("3. User-3")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice in ['1', '2', '3']:
            user_name = f"user{choice}"
            password = input("Enter Password: ")
            if authenticate_user(user_name, password):
                user_menu(user_name)
        elif choice == '4':
            code_running = False
        else:
            print("Enter a valid choice.")
        print("\nThank You! Have a nice day.")

if __name__ == '__main__':
    main()
