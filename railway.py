users = {
    "user1": {"password": "11192081", "bookings": []},
    "user2": {"password": "22114198", "bookings": []},
    "user3": {"password": "1358201", "bookings": []}
}

trains = {
    "101": {"name": "Express A", "seats": 5},
    "102": {"name": "Express B", "seats": 3},
    "103": {"name": "Express C", "seats": 4}
}

def show_bookings(bookings):
    if not bookings:
        print("No bookings found.")
    else:
        print("Your Bookings:")
        for booking in bookings:
            print(f"Train {booking['train_id']} - {booking['train_name']} (Seats: {booking['seats']})")

def book_ticket(user_name):
    print("Available Trains:")
    for train_id, train in trains.items():
        print(f"Train {train_id}: {train['name']} - Available Seats: {train['seats']}")

    train_id = input("Enter the Train ID to book: ")
    if train_id not in trains:
        print("Invalid Train ID.")
        return

    seats_to_book = int(input("Enter the number of seats to book: "))
    if seats_to_book <= 0:
        print("Invalid number of seats.")
    elif trains[train_id]["seats"] >= seats_to_book:
        trains[train_id]["seats"] -= seats_to_book
        booking_info = {"train_id": train_id, "train_name": trains[train_id]["name"], "seats": seats_to_book}
        users[user_name]["bookings"].append(booking_info)
        print(f"Successfully booked {seats_to_book} seat(s) on {trains[train_id]['name']}.")
    else:
        print("Not enough seats available.")

def cancel_ticket(user_name):
    if not users[user_name]["bookings"]:
        print("You have no bookings to cancel.")
        return

    print("Your Bookings:")
    for idx, booking in enumerate(users[user_name]["bookings"], 1):
        print(f"{idx}. Train {booking['train_id']} - {booking['train_name']} (Seats: {booking['seats']})")

    choice = int(input("Enter the booking number to cancel: ")) - 1
    if 0 <= choice < len(users[user_name]["bookings"]):
        canceled_booking = users[user_name]["bookings"].pop(choice)
        trains[canceled_booking['train_id']]["seats"] += canceled_booking['seats']
        print(f"Canceled booking on {canceled_booking['train_name']}.")
    else:
        print("Invalid choice.")

def authenticate_user(user_name, password):
    if users[user_name]["password"] == password:
        print("Login Successful")
        return True
    else:
        print("Incorrect Password. Access Denied.")
        return False

def usermenu(user_name):
    is_running = True
    while is_running:
        print("\n1. Show Bookings")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_bookings(users[user_name]["bookings"])
        elif choice == '2':
            book_ticket(user_name)
        elif choice == '3':
            cancel_ticket(user_name)
        elif choice == '4':
            return False
        else:
            print("Enter a valid choice.")
    return True

def main():
    code_running = True
    while code_running:
        print(" *** Railway Reservation System *** \n")
        print("1. User-1")
        print("2. User-2")
        print("3. User-3")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice in ['1', '2', '3']:
            user_name = f"user{choice}"
            password = input("Enter Password: ")
            if authenticate_user(user_name, password):
                usermenu(user_name)
        elif choice == '4':
            code_running = False
        else:
            print("Enter a valid choice.")
        print("Thank you! Have a nice day.")

if __name__ == '__main__':
    main()
