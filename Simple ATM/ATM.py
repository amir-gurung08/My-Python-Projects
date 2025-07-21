from random import randint as ran


class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no


    def deposit(self,new_balance):
        total_balance = self.balance + new_balance
        print(f"Your Balance was {self.balance}\nAfter Deposit {new_balance} in account {self.account_no}, Your Total Balance is {total_balance}")

    def withdraw(self, with_balance):
        if self.balance < with_balance:
             print("Insufficent Balance")
        else:
            total_balance = self.balance-with_balance
            print(f"Your Balance was {self.balance}\nAfter Withdrawing {with_balance} from account {self.account_no}, Your Total Balance is {total_balance}")
acc1 = Account(ran(20000, 100000), 130100000037201)

def how_depo():
     d = int(input("Enter the Amount: "))
     acc1.deposit(d)
def how_with():
     w = int(input("Enter the Amount: "))
     acc1.withdraw(w)


def main():
    print("1. Deposit\n2. Withdraw")
    user = int(input("Your Want to Deposit or Withdraw the cash: "))
    if user == 1:
        how_depo()
    elif user == 2:
        how_with()
    else:
        print("Invalid Option")


main() #Calling All the program