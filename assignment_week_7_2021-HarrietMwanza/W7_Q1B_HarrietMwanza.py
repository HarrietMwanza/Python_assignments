class Bank:
    def __init__(self, name, balance, accnum, pin):
        self.balance = balance
        self.name = name
        self.pin = pin
        self.accnum = accnum

    # function to ask for user current balance
    def print_current_balance(self):
        print('Your Current balance : {}'.format(self.balance))

    # function to ask user if they want to deposit
    def deposit(self):
        self.balance += float(input('Hello {}, please enter amount to deposit : '.format(self.name)))
        self.print_current_balance()

    # function to ask if user wants to withdraw money
    def withdraw(self):
        amount_to_withdraw = float(input('Enter amount to withdraw : '))

        if amount_to_withdraw > self.balance:
            print('Insufficient Balance !!')
        else:
            self.balance -= amount_to_withdraw

        self.print_current_balance()

# This method checks for user pin and account number
    def login(self, x, y):
        if x == self.pin and y == self.accnum:
            return True
        else:
           return False
