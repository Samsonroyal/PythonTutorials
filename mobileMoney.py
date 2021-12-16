# Python program to mimic the mobile money system
# Displays a menu of options to the user
# to choose from.
list = ["1.Send Money", "2.Check Balance", "3.Withraw Money", "4.Pay Bill","5.My Account"]
a = ["1.Airtel and other number", "2.MTN number ", "3.UTL number", "4.International transfer","0.Back"]
print('\n'.join(map(str, list)))

#Prompt the user to enter phone number in order to send money
def sendMoney():
    pin=2025
    balance=7000000
    number=256752330715
    reply = input("Enter your choice:")
    print("reply")
    if reply == "1":
        print('\n'.join(map(str, a)))
        if reply == "1, 2, 3, 4":
            print("Reply")
            if reply == "1":
                print("Enter the Airtel number:")
            elif reply == "2":
                print("Enter the MTN number:")
            elif reply == "3":
                print("Enter the UTL number:")
            elif reply == "4":
                print("Enter the international number:")
            else:
                print("Incorrect number please try again")
    if number == 256752330715:
        print("Enter the amount you want to send:")
    amount = int(input())
    if amount > balance:
        print("You have insufficient funds to complete the transaction!")
    else:
        print("Input your pin:")
        if pin ==2025:
            print("Transaction completed successfuly.", amount, "sent to",number)
        remainingBalance = balance - amount
        print("Your account balance is now",remainingBalance,"UGX")
        balance = remainingBalance
sendMoney()
        
