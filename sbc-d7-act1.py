import random

class BankAccount:
    def __init__(self, user_id, balance=1000):
        self.user_id = user_id
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance is {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. New balance is {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

class Bank:
    def __init__(self):
        self.accounts = {}

    def generate_user_id(self):
        user_id = f"{random.randint(1000, 9999)}"
        while user_id in self.accounts:
            user_id = f"{random.randint(1000, 9999)}"
        return user_id

    def create_account(self, initial_balance=1000):
        user_id = self.generate_user_id()
        account = BankAccount(user_id, initial_balance)
        self.accounts[user_id] = account
        return f"Account created successfully. User ID: {user_id}, Balance: {account.check_balance()}"

    def delete_account(self, user_id):
        if user_id in self.accounts:
            del self.accounts[user_id]
            return f"Account {user_id} deleted successfully."
        else:
            return "Account not found."

# Example usage:
bank = Bank()

def main_menu():
    while True:
        print("\nWelcome to the Bank!")
        print("1. Create an account")
        print("2. Log in to existing account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            initial_balance = float(input("Enter the initial balance: "))
            print(bank.create_account(initial_balance))
        elif choice == '2':
            user_id = input("Enter your User ID: ")
            if user_id in bank.accounts:
                account_menu(bank.accounts[user_id])
            else:
                print("Account not found. Please try again.")
        elif choice == '3':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

def account_menu(account):
    while True:
        print("\nAccount Menu")
        print(f"User ID: {account.user_id}, Balance: {account.check_balance()}")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Delete account")
        print("5. Log out")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Current balance: {account.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            print(account.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            print(account.withdraw(amount))
        elif choice == '4':
            confirm = input("Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == 'yes':
                print(bank.delete_account(account.user_id))
                break
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
