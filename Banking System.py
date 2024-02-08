# -----------------------------
# Banking Managment System 

print("\n\n\t\tWelcome to JS Bank\n\n")

accounts = []      # Accounts Container

def loginAccount():
    name = input("Enter Your Name: ")

    index = -1
    for i, account in enumerate(accounts):
        if account['name'] == name:
            index = i
            break

    if index == -1:
        print("\nAccount not found. \n(Create Account 1st & Try Again) \n")
        return None

    pin = int(input("Enter Your PIN-Code: "))  

    while True:
        if accounts[index]['pin'] == pin:
            print("Login successful.")
            return index
        else:
            print("Incorrect PIN-Code... \nTry Again")
            pin = int(input("Enter Your PIN-Code: ")) 

def createAccount():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    balance = int(input("Enter your balance: "))
    pin = int(input("Enter PIN-Code: "))
    
    account = {
        'name': name,
        'age': age,
        'balance': balance,
        'pin': pin
    }
    accounts.append(account)
    print("\nAccount Created... OK\n")

def checkBalance(account):
    print("\nCurrent balance is:", account['balance'], '\n')

def depositAmount(account):
    amount = int(input("Enter amount to deposit: "))
    account['balance'] += amount
    print("\nDeposited successfully... OK \nUpdated balance:", account['balance'], '\n')

def withdrawAmount(account):
    amount = int(input("Enter amount to withdraw: "))
    if account['balance'] >= amount:
        account['balance'] -= amount
        print("\nWithdrawal successfully... OK \nUpdated balance:", account['balance'], '\n')
    else:
        print("Not enough balance in Your account...")

while True:
    currentAccount = -1
    print("0. Login Account")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "0":
        currentAccount = loginAccount()
        if currentAccount is not None:
            continue
    elif choice == "1":
        createAccount()
    elif choice == "2":
        if len(accounts) != 0:  
            checkBalance(accounts[currentAccount])
        else:
            print("\n You have to Login 1st... Try again\n")
    elif choice == "3":
        if len(accounts) != 0:
            depositAmount(accounts[currentAccount])
        else:
            print("\n You have to Login 1st... Try again\n")
    elif choice == "4":
        if len(accounts) != 0:
            withdrawAmount(accounts[currentAccount])
        else:
            print("\n You have to Login 1st... Try again\n")
    elif choice == "5":
        print("\n Exit... OK\n")
        break
    else:
        print("Choose from above choices (i.e., 0, 1, 2, etc.)")
