# we import the file with the accounts work flow
from W7_Q1B_HarrietMwanza import Bank

# our class for savings account
class Savings_account(Bank):
    def __init__(self, name, accnum,balance, duration,pin):
        super().__init__(name, accnum,balance, pin)
        self.duration = duration

# we have our method to do the withdraw in the savings account
# we have duration which we get from the user after prompting them
# we have the rate which we divide by 100 and get 0.03

    def withdraw(self):
        if self.duration >= 6:
            rate_interest1 = 0.03
            t = (self.balance * rate_interest1*self.duration)
            self.balance = (t + self.balance)
            print("Your balance is {}".format(self.balance))

            withdrawamt = int(input("How much do you want to withdraw?"))
            if withdrawamt <= self.balance:
                print("You have successfully withdraw{}".format(withdrawamt))
                self.balance = self.balance - withdrawamt
                print("You balance is {}".format(self.balance))
            else:
                print("Insufficient funds. your balance{}".format(self.balance))
        else:
            print("You can only withdraw after 6 months")

# We have a method that prints out the user balance
    def print_current_balance(self):
        rate_interest1 = 0.03
        t = (self.balance * rate_interest1*self.duration)
        self.balance = (t + self.balance)
        print("Your balance is {}".format(self.balance))


# our class for current account
class Current_account(Bank):
    def __init__(self, name, accnum, balance, duration, pin):
        super().__init__(name, accnum, balance, pin)
        self.duration = duration

# our method to withdraw from user current account
# we have duration which we get from the user after prompting them
# we have the rate which we divide my 100 and get 0.01

    def withdraw(self):
        if self.duration >= 1:
            rate_interest1 = 0.01
            t = (self.balance * rate_interest1 * self.duration)
            self.balance = (t + self.balance)
            print("Your balance is {}".format(self.balance))

            withdrawamt = int(input("How much do you want to withdraw?"))
            if withdrawamt <= self.balance:
                print("You have successfully withdraw{}".format(withdrawamt))
                self.balance = self.balance - withdrawamt
                print("You balance is {}".format(self.balance))
            else:
                print("Insufficient funds. your balance{}".format(self.balance))
        else:
            print("You can only withdraw after 6 months")

# Our method to show the balance that the ser has
    def print_current_balance(self):
        rate_interest1 = 0.01
        t = (self.balance * rate_interest1 * self.duration)
        self.balance = (t + self.balance)
        print("Your balance is {}".format(self.balance))

