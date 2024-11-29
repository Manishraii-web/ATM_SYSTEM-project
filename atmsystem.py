 # ATM System
balance = 10000
pin = 2024

print("+*Inset your pin number+*")
pin_num = int(input("Enter you pin number, PLease..\n"))

if pin_num == pin:
    while True :
     print(''' 
          1 - check balance
          2 - Deposit
          3 - Withdraw
          4 - Exit
          ''')
     option = int(input("choice your option \n"))
     if option == 1:
        print(f"your bank balance is  {balance}")
     elif option ==2 :
        deposit_amt = int(input("Enter your desposit amount \n"))
        balance = balance + deposit_amt 
        print(f"your updated amount is {balance}")
     elif option == 3 :
        withdraw_amt = int(input("Enter your withdrawl amount \n")) 
        if balance < withdraw_amt:
            print("insufficient balance")
            break
        else:
            withdraw_amt = balance - withdraw_amt
        print(f"your updated amount is {balance}")
        break
     elif option ==4:
        break
        
else:
    print("pin number incorrected")