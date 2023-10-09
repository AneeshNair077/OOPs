class atm:
    def __init__(self, name, number):
        self.accn=name
        self.accno=number
    def deposit(self):
        self.bal=0
        self.dep=int(input("Enter amount to be deposited "))
        self.bal=self.dep+self.bal
        print("Amount deposited succesfully")
    def withdraw(self):
        self.w=int(input("Enter amount to withdraw "))
        if(self.w<self.bal):
            self.bal=self.bal-self.w
            print("Amount withdrawed")
        else:
            print("Amount cannot be withdrawn")
    def view(self):
        print("Balance is:",self.bal)
accname=input("Enter account holder name ")
accno=int(input("Enter account number "))
a=atm(accname,accno)
print("ACCOUNT DETAILS\n")
print("Account Holder:",accname)
print("Account Number:",accno)
print("1.Deposit money\n2.Withdraw money\n3.View Balance\n4.Exit")
ch=int(input("Enter choice "))
while(ch!=0):
  if(ch==1):
      a.deposit()
  elif(ch==2):
      a.withdraw()
  elif(ch==3):
      a.view()
  elif(ch==4):
      print("Exiting")
      break
  ch=int(input("Enter choice "))
