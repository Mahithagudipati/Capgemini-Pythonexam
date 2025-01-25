def Check_Balance(actual_amount):
    print("Amount :",actual_amount)

def Deposit_money(actual_amount):
    amount_deposit=int(input("Enter the amount to be deposited: "))
    actual_amount=actual_amount+amount_deposit
    print("Amount after deposit : ", actual_amount)
    return actual_amount

def withdraw_money(actual_amount):
    if(actual_amount==0):
        print("Zero balance")
    else:
        amount_withdraw=int(input("Enter the amount to be withdrawn: "))
        if(actual_amount<=amount_withdraw):
            print("Insufficient balance")
        else:
            actual_amount=actual_amount-amount_withdraw
            print("Amount after withdrawal: ",actual_amount)
    return actual_amount

def exit_fun():
    return 1
actual_amount=2000
while(True):
    print(" 1.Check Balance \n2.Deposit Money \n3.Withdraw Money \n4.Exit")
    choice=int(input("Enter the choice: "))
    if choice==1:
        Check_Balance(actual_amount)
    elif choice==2:
            actual_amount=Deposit_money(actual_amount)
    elif choice==3:
            actual_amount=withdraw_money(actual_amount)
    elif choice==4:
            exit_fun()
            break
    else:
            print("Invalid choice")