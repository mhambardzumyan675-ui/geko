class BankAccount:
    def __init__(self,owner):
        self.owner=owner
        self.balance=0
    
    def deposit(self,amount):
         if amount<=0:
            print("Wrong amount")
         else:
             self.balance+=amount
             print("Amount added")

    def withdraw(self,amount):
        if amount<=0:
            print("Wrong amount")
        elif amount>self.balance:
            print("Insufficient funds")
        else:
             self.balance-=amount
             print(f"{amount}֏ was deducted from the balance")

    def transfer(self,other,amount):
        if amount<=0 and amount>self.balance:
            print("Insufficient funds")
        else:
             other.balance+=amount
             self.balance-=amount
             print("Amount transfered to other balance")

    def showinfo(self):
        print(f"Owner:{self.owner}/Balance:{self.balance}")

accounts={}

while True:
    print("""
        1 — Create account
        2 — Deposit money
        3 — Withdraw money
        4 — Transfer money
        5 — Show one account
        6 — Show all accounts
        7 — Delete account
        8 — Show the richest customer
        9 — Statistics
        0 — Exit
""")
    
    choice=int(input("Choose action:"))
    if choice==1:
        name=input("Enter owner name:")
        if name in accounts:
            print(f"Owner {name} already added!")
        else:
             accounts[name]=BankAccount(name)
             print("Account created!")
    elif choice==2:
        name=input("Enter account name:")
        if name not in accounts:
            print("Not found account")
        else:
            amount=int(input("Enter amount:"))
            accounts[name].deposit(amount)

    elif choice==3:
        name=input("Enter account name:")
        if name in accounts:
            amount=int(input("Enter amount:"))
            accounts[name].withdraw(amount)
        else:
             print("Not found Account")

    elif choice==4:
        sender=input("Enter sender name:")
        receiver=input("Enter receiver name:")
        if sender and receiver in accounts:
           amount=int(input(f"Enter amount to transfer from {sender} to {receiver}:"))
           accounts[sender].transfer(accounts[receiver],amount)
        else:
            print("Not found Account")
        
    elif choice==5:
        show=input("Enter Account name:")
        if show in accounts:
            accounts[show].showinfo()
        else:
             print("Not found Account")
            
    elif choice==6:
        if len(accounts)==0:
            print("Not added accounts yet!")
        else:
             for account in accounts.values():
                 account.showinfo()

    elif choice==7:
        name=input("Enter account name:")
        if name in accounts:
            del accounts[name]
            print(f"Account {name} deleted")
        else:
            print("Not found account")

    elif choice==8:
        if accounts:
            richest=max(accounts.values(),key=lambda x: x.balance)
            print(f"Richest owner:{richest.owner}")

    elif choice==9:
        count=len(accounts)
        total_balance=sum(acc.balance for acc in accounts.values())
        
        if count>0:
            avg=total_balance/count
        else:
            avg=None

        zero=0
        for acc in accounts.values():
            if acc.balance==0:
                zero+=1
        print("Accounts count:",count)
        print("Total balance:",total_balance)
        print("Average balance:",avg)
        print("Accounts with zero balance:",zero)

    elif choice==0:
        print("Exit")
    else:
        print("Wrong action")




        
            

                 
    


