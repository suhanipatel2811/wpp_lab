class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Account number
        self.balance = balance  # Account balance (default is 0)

    def deposit(self, amount):
        """Method to deposit funds into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Method to withdraw funds from the account"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        """Method to display account details"""
        print(f"\nAccount Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")

# Function to take user input and interact with the BankAccount class
def main():
    print("Welcome to the Bank Account System!")
    
    account_number = input("Enter your account number: ")
    balance = float(input("Enter initial balance (default 0): ") or 0)

    # Create a BankAccount object
    account = BankAccount(account_number, balance)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Details")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.display()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

# Run the program
if __name__ == "__main__":
    main()
