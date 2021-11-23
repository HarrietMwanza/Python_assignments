from W7_Q1B_HarrietMwanza import Bank
import random

allaccounts = []


# here is the menu to be shown to the user
# our user menu

while True:
    print("========== WELCOME TO DANGOTE BANKING SYSTEM ==========")
    print("========== (a). To Open New Client Account")
    print("======(b)To log into your account=====")
    print("========== (c). To Quit ")
    EnterLetter = input("Select a Letter from the Above Box menu : ")
    if EnterLetter == "a":
        name = input("Write Your Fullname : ")
        pin = input("Please Write a Pin to Secure your Account : ")
        while True:
            bal = int(input('How much is your starting depositing, minimum 100'))
            if bal < 100:
                print("Deposit at least 100")
                continue
            break
        newAc = Bank(name, bal, random.randint(1111, 9999), pin)
        allaccounts.append(newAc)
        print('Welcome ' + newAc.name + ' your account number is ' + str(newAc.accnum))

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
        print("Bye")
        break
