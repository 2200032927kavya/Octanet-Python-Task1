class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id.lower()  # Normalize to lowercase
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        print(f"${amount} deposited successfully. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"${amount} withdrawn successfully. Current balance: ${self.balance}")
        else:
            print("Insufficient balance!")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred: ${amount} to {recipient.user_id}")
            recipient.transaction_history.append(f"Received: ${amount} from {self.user_id}")
            print(f"${amount} transferred successfully to {recipient.user_id}.")
        else:
            print("Insufficient balance!")

    def show_transactions(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions available.")

class ATM:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, user_id, pin, balance=0):
        self.users[user_id.lower()] = User(user_id, pin, balance)

    def authenticate_user(self, user_id, pin):
        user_id = user_id.lower()  # Normalize to lowercase
        if user_id in self.users and self.users[user_id].check_pin(pin):
            self.current_user = self.users[user_id]
            return True
        return False

    def main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.current_user.show_transactions()
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                self.current_user.withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                self.current_user.deposit(amount)
            elif choice == '4':
                recipient_id = input("Enter recipient user ID: ")
                if recipient_id.lower() in self.users:
                    amount = float(input("Enter amount to transfer: "))
                    self.current_user.transfer(amount, self.users[recipient_id.lower()])
                else:
                    print("Recipient user ID not found.")
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                self.current_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def start(self):
        print("Welcome to the ATM!")
        user_id = input("Enter user ID: ")
        pin = input("Enter PIN: ")
        if self.authenticate_user(user_id, pin):
            print("Login successful!")
            self.main_menu()
        else:
            print("Invalid user ID or PIN. Please try again.")

# Example usage:
atm = ATM()
atm.add_user("user1", "1234", 1000)
atm.add_user("user2", "5678", 500)

atm.start()
