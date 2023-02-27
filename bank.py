class bankac():
    def custdet(self,cname,acno,actype,bal):
        self.cname=cname
        self.acno=acno
        self.actype=actype
        self.bal=bal
    def deposit(self,amt):
        self.bal=self.bal+amt
    def withdraw(self,amt):
        if self.bal<amt:
            return("false")
        else:
            self.bal=self.bal-amt
    def display(self):
        print("Customer Name:",self.cname)
        print("Account Number:",self.acno)
        print("Account type:",self.actype)
        print("Balance:",self.bal)
obj=bankac()
ch=0
while(ch!=5):
    print("1.store c details")
    print("2.deposit")
    print("3.withraw")
    print("4.display")
    ch=int(input("Enter a choice"))
    if ch==1:
        cname=input("Enter name")
        acno=input("Enter ac no:")
        actype=input("Enter actype")
        bal=int(input("enter balance:"))
        obj.custdet(cname,acno,actype,bal)
    elif ch==2:
        amt=int(input("Enter the amount to deposit"))
        obj.deposit(amt)
    elif ch==3:
        amt=int(input("Enter the amount to withdraw"))
        obj.withdraw(amt)
    elif ch==4:
        obj.display()
    else:
        print("invalid choice:")
