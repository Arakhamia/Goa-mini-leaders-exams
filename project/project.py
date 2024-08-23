# Bank System:

# 1.create account
# 2.Deposit
# 3.Withdraw
# 4.Exit

def bank():
    gmail = input("Lets create an account of the bank. First, enter your E-mail: ")
    password = input("Now enter your password: ")
    name = input("Enter your name: ")
    age = int(input("Now enter your age: "))

    if age < 18:
        print("You are too young! you can't create an account!")
        exit
    else:
        print("Your account is created, welcome" + " " + name + "!")

        account = [gmail, password, name, age]
        balance = 100

        print("Your balance is" + " " + str(balance))

        print("Deposit money to balance - 1")
        print("Withdraw money from balance - 2")
        print("Exit - 3")
    
        choise = int(input("Enter the number (1 deposit money, 2 withdraw, 3 exit): "))
    
        if choise == 1:
            input("Enter your card number: ")
            input("Enter your card passcode: ")
            balance1 = int(input("Enter the deposit cash: "))
            balance = balance1 + balance
            print("Your balance is: " + str(balance))

        elif choise == 2:
            input("Enter your card number: ")
            input("Enter your card passcode: ")
            balance2 = int(input("Enter the withdraw cash: "))
            if balance2 < balance:
                balance4 = balance - balance2
                print("Your balance is: " + str(balance4))
            elif balance2 > balance:
                print("You cannot withdraw more money than the current balance.")
            print("Exit - 3")
            num3 = int(input("Enter number 3 to exit: "))
            if num3 == 3:
                exit
            else:
                print("inccorect symbol.try again")

        elif choise == 3:
            exit
    

bank()