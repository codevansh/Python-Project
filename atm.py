users={
    "user1":{"password":"11192081","balance":0},
    "user2":{"password":"22114198","balance":0},
    "user3":{"password":"1358201","balance":0}
}

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter a Amount to be deposited:"))
    if(amount < 0):
        print("That's not a Valid Amount")
        return 0
    else:
        return amount
    

def withdraw(balance):
    amount = float(input("Enter amount to be withdraw:"))
    
    if(amount > balance):
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("Amount cannot be negative")
        return 0
    else:
        return amount

def authenticate_user(user_name , password):
    if(users[user_name]["password"] == password):
        print("Login Successfull")
        return True
    else:
        print("Incorrect Password. Access denied")
        return False
    
def usermenu(user_name):
    is_running = True
    while is_running:
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw Money")
        print("4.Exit")
        choice=input("Enter your Choice (1-4):")

        if choice == '1':
            show_balance(users[user_name]["balance"])
        elif choice =='2':
           users[user_name]["balance"] = users[user_name]["balance"] + deposit()
        elif choice =='3':
            users[user_name]["balance"] = users[user_name]["balance"] - withdraw(users[user_name]["balance"])
        elif choice =='4':
            return False
        else:
            print("Enter a Valid Choice")
    return True
    
def main():
    code_running = True
    while code_running:
        print(" *** Banking Program *** \n")
        print("1.User-1")
        print("2.User-2")
        print("3.User-3")
        print("4.Exit")
        choice=input("Enter your Choice (1-4):")
        
        if choice in ['1','2','3']:
            user_name = f"user{choice}"
            password = input("Enter Password:")
            if authenticate_user(user_name,password):
                usermenu(user_name)
        elif choice == '4':
            code_running=False
        else:
            print("Enter a Valid choice")
        print("Thank You! Have a nice day")
           
           
if __name__ == '__main__':
    main()