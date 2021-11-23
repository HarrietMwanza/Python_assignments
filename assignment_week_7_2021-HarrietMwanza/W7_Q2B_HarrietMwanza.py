from W7_Q2A_HarrietMwanza import Savings_account, Current_account
import random

# We have a list that will hold all user names, account numbers, pins and the amounts they have
# we append all user input when prompted onto the list

allaccounts = []

# We have a method that allows user to transfer money to another person
# We prompt user to put in receiver account number, which will be checked for in the list
# We have a variable that holds in our results from the list once we find the receiver information user has put in
# To achieve this we use the senderAccount is equal to none to check in our list

def transfer(sender, receiver, amount):
    senderAccount = None
    receiverAccount = None
    for acc in allaccounts:
        if sender == acc.accnum:
            senderAccount = acc
        elif receiver == acc.accnum:
            receiverAccount = acc

    if senderAccount is None or receiverAccount is None:
        print('Invalid sender or receiver')
    else:
        if amount > senderAccount.balance:
            print("insufficient funds!")
        else:
            senderAccount.balance -= amount
            receiverAccount.balance += amount
            print("Amount sent " + str(amount) + ' new balance is  ' + str(senderAccount.balance))

# This part of the code displays menu to user
while True:
    print("WELCOME TO DANGOTE BANKING SYSTEM")
    print("(a). To Open New Client Account")
    print("(b)To log into your account")
    print("(c). To Quit ")
    EnterLetter = input("Select a Letter from the Above Box menu : ")
    if EnterLetter == "a":
        typeAcc = input("Choose type a) current b) saving")
        if typeAcc == 'a':
            name = input("Write Your Fullname : ")
            pin = input("Please Write a Pin to Secure your Account : ")
            while True:
                bal = int(input('How much is your starting depositing, minimum 100'))
                if bal < 100:
                    print("Deposit at least 100")
                    continue
                break
            newAc = Current_account(name,random.randint(1111, 9999),bal,8,pin)
            allaccounts.append(newAc)
            print('Welcome ' + newAc.name + ' your account number is ' + str(newAc.accnum))
        elif typeAcc == 'b':
            name = input("Write Your Fullname : ")
            pin = input("Please Write a Pin to Secure your Account : ")
            while True:
                bal = int(input('How much is your starting depositing, minimum 100'))
                if bal < 100:
                    print("Deposit at least 100")
                    continue
                break
            # newAc = Bank(name, bal, random.randint(1111, 9999), pin)
            newAc = Savings_account(name, random.randint(1111, 9999),bal,10,pin)
            allaccounts.append(newAc)
            print('Welcome ' + newAc.name + ' your account number is ' + str(newAc.accnum))
        else:
            print("Invalid")

    elif EnterLetter == 'b':
        while True:
            accn = int(input('Enter account num'))
            enterPin = input("Enter your pin")
            activeAccount = None
            for account in allaccounts:
                if accn == account.accnum:
                    activeAccount = account

            if activeAccount is None:
                print("Wrong account")
                continue

            if activeAccount.login(enterPin, accn) is False:
                print('Wrong login details')
                continue

# This part of the code displays a second menu to user for more functions
            while True:
                input_value = int(input(
                    'Pick an option from the ones below:\n1 to see your balance,\n2 to deposit\n3 to withdraw\n4 to transfer \n5 Exit: '))
                if input_value == 1:
                    activeAccount.print_current_balance()
                elif input_value == 2:
                    activeAccount.deposit()
                elif input_value == 3:
                    activeAccount.withdraw()
                elif input_value == 4:
                    receiverAcc = int(input("Enter receiver account"))
                    amountSend = float(input("Enter amount to send"))
                    transfer(activeAccount.accnum, receiverAcc, amountSend)
                elif input_value == 5:
                    break
                else:
                    print("Wrong input")
                    continue
            break

    else:
        print("Bye!")
        break