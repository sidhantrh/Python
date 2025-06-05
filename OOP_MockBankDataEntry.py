# main class Account
class Account:
    # main function for the class that holds the name, id, and balance
    def __init__(self, name, ID, balance):
        self.name = name
        self.ID = ID
        self.balance = balance
    
    # deposit method, changes the account to add to the amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    # withdraw method, changes the account to subtract the amount 
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    # displays the account information
    def display(self):
        print(f"Name: {self.name}\nType: Standard\nID: {self.ID}\nBalance: ${self.balance}")

# student account class that inherits from main account class
class StudentAccount(Account):
    # constructor for student account, includes school and $10 bonus
    def __init__(self, name, ID, balance, school):
        super().__init__(name, ID, balance + 10)  # Adds the $10 bonus
        self.school = school

    # displays the student account information
    def display(self):
        print(f"Name: {self.name}\nType: Student\nID: {self.ID}\nBalance: ${self.balance}\nSchool: {self.school}")

# function reverses a string
def manual_reverse(s):
    reversed_s = ''  # empty string to build reversed string
    for char in s[::-1]:  # loop through the string backwards
        reversed_s += char  # add each character to the reversed string
    return reversed_s 

# function changes the second letter of a string to 'x'
def change_second_letter(s):
    new_s = ''  # empty string to build modified string
    new_s = s[0] + 'x' + s[2:]  # keep first character, replace second with 'x', keep the rest
    return new_s

# function finds account by name or ID
def find_account(accounts, search_by, value):
    for acc in accounts:  # loop through all accounts
        if (search_by == 'name' and acc.name == value) or (search_by == 'ID' and acc.ID == value):  # match found
            return acc
    return None  # if not found

# function sort accounts by balance amount
def manual_sort(accounts):
    for i in range(len(accounts)):
        for j in range(i + 1, len(accounts)):
            if accounts[j].balance > accounts[i].balance:
                accounts[i], accounts[j] = accounts[j], accounts[i]  # swap if needed

# main program function
def main():
    accounts = []  # list to store created accounts

    print("Welcome to the Simple Banking System!")
    bank_name = input("Enter your bank name: ").strip()  # ask for bank name

    # input validation for bank name
    while bank_name == '':
        bank_name = input("Bank name cannot be empty. Enter again: ").strip()
    print(f"\nBank name saved: {bank_name}\n")  # display saved bank name

    # infinite loop to show menu until user exits
    while True:
        print("--- Main Menu ---")
        print("1. Create New Account\n2. Deposit Money\n3. Withdraw Money\n4. View All Accounts")
        print("5. Search for an Account\n6. Sort Accounts by Balance\n7. Rename Bank (Reverse/Edit)\n8. Exit")
        choice = input("Enter your choice: ").strip()  # get menu choice
        
        list_options = ['1', '2', '3', '4', '5', '6', '7', '8']
        if choice not in list_options:
            print("Invalid choice. Enter a number between 1-8.\n")
            continue  # invalid menu choice
        
        #create new account
        if choice == '1':
            if len(accounts) >= 5:
                print("Error: Cannot create more than 5 accounts.\n")
                continue
            
            # creating a new account
            print("\n--- Create New Account ---")
            name = input("Enter account holder's name: ").strip()
            while name == '':
                name = input("Name cannot be empty. Enter again: ").strip()

            #Asks user for account id
            ID = input("Enter account ID: ").strip()
            while ID == '' or find_account(accounts, 'ID', ID): # Looks for initial ids stored in the database
                if ID == '':
                    ID = input("ID cannot be empty. Enter again: ").strip()
                else:
                    print("Error: This account ID already exists.") #states the id already exists
                    ID = input("Enter account ID: ").strip() # Asks for id input again

            acc_type = input("Select account type (standard/student): ") #asks for 
            while acc_type is not'standard' or 'student':
                acc_type = input("Invalid type. Choose 'standard' or 'student': ").strip()

            if acc_type == 'student':
                school = input("Enter school name: ").strip()
                while school == '':
                    school = input("School name cannot be empty. Enter again: ").strip() #asks for user input if school name is not empty 

            try:
                initial = float(input("Enter initial deposit amount: ").strip()) # asks for inital deposit amount
                while initial <= 0:
                    print("Error: Deposit must be a positive amount.") # if the number is not positive, it gives an error
                    initial = float(input("Enter initial deposit amount: ").strip())
            except ValueError:
                print("Error: Invalid number. Returning to menu.\n") #returns to menu if there is an error 
                continue

            # create account based on type
            if acc_type == 'student':
                accounts.append(StudentAccount(name, ID, initial, school))
                print("\nStudent account created successfully!")
                print(f"Final Balance: ${accounts[-1].balance:.2f}\n")
            else:
                accounts.append(Account(name, ID, initial))
                print("\nStandard account created successfully!")
                print(f"Final Balance: ${accounts[-1].balance:.2f}\n")

        #2: deposit money
        elif choice == '2':
            print("\n--- Deposit Money ---")
            ID = input("Enter account ID: ").strip()
            acc = find_account(accounts, 'ID', ID)
            if acc:
                try:
                    amount = float(input("Enter amount to deposit: ").strip())
                    if acc.deposit(amount):
                        print("\nDeposit successful.")
                        print(f"New balance for {ID}: ${acc.balance:.2f}\n")
                    else:
                        print("Error: Deposit must be positive.\n")
                except ValueError:
                    print("Error: Invalid number.\n")
            else:
                print(f"Error: No account found with ID '{ID}'.\n")

        #3: withdraw money
        elif choice == '3':
            print("\n--- Withdraw Money ---")
            ID = input("Enter account ID: ").strip()
            acc = find_account(accounts, 'ID', ID)
            if acc:
                try:
                    amount = float(input("Enter amount to withdraw: ").strip())
                    if acc.withdraw(amount):
                        print("\nWithdrawal successful.")
                        print(f"New balance for {ID}: ${acc.balance:.2f}\n")
                    else:
                        if amount <= 0:
                            print("Error: Withdrawal must be positive.\n")
                        else:
                            print("Error: Insufficient funds.\n")
                except ValueError:
                    print("Error: Invalid number.\n")
            else:
                print(f"Error: No account found with ID '{ID}'.\n")

        #4: view all accounts
        elif choice == '4':
            print("\n--- All Accounts ---")
            for idx, acc in enumerate(accounts, 1):
                print(f"{idx}.", end=" ")
                acc.display()
                print()

        #5: search for account
        elif choice == '5':
            print("\n--- Search for Account ---")
            by = input("Search by (1) Name or (2) ID: ").strip()
            if by == '1':
                name = input("Enter account holder's name: ").strip()
                acc = find_account(accounts, 'name', name)
            elif by == '2':
                ID = input("Enter account ID: ").strip()
                acc = find_account(accounts, 'ID', ID)
            else:
                print("Invalid search option.\n")
                continue

            if acc:
                print("\nAccount found:")
                acc.display()
                print()
            else:
                print("Error: No account found.\n")

        #6: sort accounts
        elif choice == '6':
            print("\n--- Sort Accounts by Balance (Descending) ---")
            manual_sort(accounts)
            print("Accounts sorted:")
            for idx, acc in enumerate(accounts, 1):
                print(f"{idx}. {acc.name} - {acc.ID} - ${acc.balance:.2f}")
            print()

        #7: renames the bank
        elif choice == '7':
            print("\n--- Rename Bank ---")
            print(f"Current bank name: {bank_name}")
            reversed_name = manual_reverse(bank_name)
            print(f"Reversed name: {reversed_name}")
            modified_name = change_second_letter(bank_name)
            print(f"Modified name (2nd character to 'x'): {modified_name}")
            bank_name = modified_name
            print(f"\nBank name updated to: {bank_name}\n")

        #8: exit the system
        elif choice == '8':
            print(f"\nThank you for using {bank_name}. Goodbye!")
            break

# main code runs
if __name__ == "__main__":
    main()
