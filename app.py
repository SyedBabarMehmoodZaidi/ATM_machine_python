class ATM:
    def __init__(self):
        """"
        Initialize the ATM with a default pin and balance.
        """
        self.pin = "1234"  # Default pin
        self.balance = 1000.0
        self.is_authenticated = False

    def check_pin(self, input_pin):
        """
        Check if the entered pin is correct.
        """
        if input_pin == self.pin:
            self.is_authenticated = True
            print("✅PIN accepted. You can now access your account.\n")
        else:
            print("❌Incorrect PIN. Please try again.")


    def check_balance(self):
        """
        Display the current balance.
        """
        if self.is_authenticated:
            print(f"💰Your current balance: Rs. {self.balance:.2f}\n")
        else:
            print("❌Please enter the correct PIN first.\n")

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                print(f"✅Deposited Rs. {amount:.2f}. New balance: Rs. {self.balance:.2f}\n")
            else:
                print("❌Invalid deposit amount. Please enter a positive number.\n")
        else:
            print("❌Please enter the correct PIN first.\n")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        """
        if self.is_authenticated:
            if amount <= 0:
                print("❌Invalid withdrawal amount. Please enter a positive number.\n")
            elif amount > self.balance:
                print("❌Insufficient balance. Please enter a smaller amount.\n")
            else:
                self.balance -= amount
                print(f"✅Withdrew Rs. {amount:.2f} withdraw successfully.")
                print(f"💰Your current balance: Rs. {self.balance:.2f}\n")           

        else:
            print("❌Please enter the correct PIN first.\n")

    def exit(self):
        """
        Exit the ATM session.
        """
        print("👋Thank you for using the ATM. Goodbye!\n")
        return False #Indicate to exit the loop
    
    def menu(self):
        """
        Display the ATM menu and handle user interactions.
        """
        print("===== Welcome to the ATM =====")
        attempts = 0
        while attempts < 3:
            input_pin = input("🔑Please enter your 4-digit PIN: ")
            if input_pin == self.pin:
                self.is_authenticated = True
                print("✅PIN accepted. You can now access your account.\n")
                break
            else:
                attempts += 1
                print(f"❌Incorrect PIN. You have {3 - attempts} attempts left.\n")
        else:
            print("❌Too many incorrect attempts. Exiting the ATM.\n")
            return
        while True:
            print("===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Please select an option (1-4): ")   

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("💵Enter the amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print("❌Invalid input. Please enter a valid number.\n")
            elif choice == "3":
                try:
                    amount = float(input("💵Enter the amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print("❌Invalid input. Please enter a valid number.\n")            
            elif choice == "4": 
                if not self.exit():
                    break
            else:
                print("❌Invalid selection. Please select a valid option.\n")

if __name__ == "__main__":
    atm = ATM()
    atm.menu()


   
