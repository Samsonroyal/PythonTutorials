#Initialising function to control login to withdraw money.
def withdrawMoney():
    name="Nagawa Annet"
    pin=2021
    balance=7000000
    nameEntered =input("Please enter your username:")
    if nameEntered == name:
        pinEntered=int(input("Please enter your pin:"))
        if pinEntered == pin:
            print("Your account balance is",balance,"UGX")
            amountToWithdraw=int(input("How much do you want to withdraw?:"))
            if amountToWithdraw > balance:
                print("You have insufficient funds to complete the transaction!")
            else:
                print("Transaction successful")
                remainingBalance= balance - amountToWithdraw
                print("Your account balance is now",remainingBalance,"UGX")
                balance = remainingBalance
        else:
            print("Incorrect pin, please try again!")
    else:
        print("Please enter a correct username!")
withdrawMoney()