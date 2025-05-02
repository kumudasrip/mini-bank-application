class Customer:
    bankname='MY BANK'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(amount,'is deposited\n')
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient balance\n')
        else:
            self.balance=self.balance-amount
            print(amount,'is withdrawn\n')
    def showbalance(self):
        print('Balance amount in your bank is:',self.balance,'\n')

print('$'*15,'Welcome to',Customer.bankname,'$'*15)
name=input('Enter your name:')
print('\n')
c=Customer(name)
while True:
    print('d-Deposit\nw-Withdraw\nb-Balance amount\ne-Exit')
    option=input('Choose your option:')
    if option.lower()=='d':
        amount=float(input('Enter amount to deposit:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('Enter amount to withdraw:'))
        c.withdraw(amount)
    elif option.lower()=='b':
        c.showbalance()
    elif option.lower()=='e':
        print('Thank you',name,'for Banking :)')
        break
    else:
        print('Please choose valid option!!\n')
        
