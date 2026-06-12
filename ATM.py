class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
            ----- ATM MENU -----
            1. Create PIN
            2. Change PIN
            3. Check Balance
            4. Withdraw
            5. Deposit
            6. Exit
            Choose an option: """).strip()

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.change_pin()
            elif user_input == '3':
                self.check_balance()
            elif user_input == '4':
                self.withdraw()
            elif user_input == '5':
                self.deposit()
            elif user_input == '6':
                print("Thank you for using the ATM. Goodbye!")
                exit()
            else:
                print("Invalid choice. Try again.")

    def create_pin(self):
        if self.pin:
            print("PIN already exists. Use 'Change PIN' instead.")
            return
        user_pin = input("Set a 4-digit PIN: ").strip()
        if not user_pin.isdigit() or len(user_pin) != 4:
            print("Invalid PIN format. Must be 4 digits.")
            return
        self.pin = user_pin

        try:
            initial_balance = float(input("Enter initial deposit amount: "))
            if initial_balance < 0:
                print("Amount cannot be negative.")
                self.pin = ''
                return
        except ValueError:
            print("Invalid amount.")
            self.pin = ''
            return

        self.balance = initial_balance
        print("PIN created successfully!")

    def change_pin(self):
        old_pin = input("Enter your current PIN: ").strip()
        if old_pin == self.pin:
            new_pin = input("Enter new PIN: ").strip()
            if not new_pin.isdigit() or len(new_pin) != 4:
                print("Invalid PIN format. Must be 4 digits.")
                return
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Incorrect PIN.")

    def check_balance(self):
        user_pin = input("Enter your PIN: ").strip()
        if user_pin == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Incorrect PIN.")

    def withdraw(self):
        user_pin = input("Enter your PIN: ").strip()
        if user_pin != self.pin:
            print("Incorrect PIN.")
            return

        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Enter a valid amount.")
                return
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def deposit(self):
        user_pin = input("Enter your PIN: ").strip()
        if user_pin != self.pin:
            print("Incorrect PIN.")
            return

        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Enter a valid amount.")
                return
        except ValueError:
            print("Invalid amount.")
            return

        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")


if __name__ == "__main__":
    obj1 = Atm()