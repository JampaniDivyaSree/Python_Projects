class Bank:

    def __init__(self,cust,acc_no,branch,IFSC):
        self.amount=10000
        self.cust=cust
        self.acc_no=acc_no
        self.branch=branch
        self.IFSC=IFSC
        print("Customer:",self.cust)
        print("Account Number:",self.acc_no)
        print("Branch:",self.branch)
        print("IFSC Code:",self.IFSC)
        

    def Credit(self,credit):
        self.amount=self.amount+credit
        print("Balance amount:",self.amount)
        self.Operations()

    def Debit(self,Debit):
        self.amount=self.amount-Debit
        if self.amount==0 or self.amount<500:
            print("No sufficient balance amount")
        else:
            print("balance:",self.amount)
        self.Operations()

    def Operations(self):
        print("Available options")
        print(" 1.credit \n 2.Debit \n 3.Exit")
        self.n=int(input("Enter your choice:"))
        if self.n==1:
            deposit=int(input("enter amount to deposit:"))
            self.Credit(deposit)
        elif self.n==2:
            draw=int(input("enter amount to draw:"))
            self.Debit(draw)
        else:
            pass
b=Bank("Hima",123456789,2,"2FDFRC300")
b.Operations()
