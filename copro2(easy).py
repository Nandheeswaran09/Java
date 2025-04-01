class bankaccount:
    def __init__(self,account,balance):
        self.account_holder=account
        self.balance=balance
    
    def deposit(self,amount):
        amo= self.balance + amount
        print(f'Deposit {amount} New Balance {amo}')
    
    def withdraw(self,amount):
        wit = self.balance - amount
        print (f'Withdraw {amount} .New balance {wit}')
    
    def check_blance(self):
        print(f'Account holder {self.account_holder} , Balance {self.balance}' )
        

c1= bankaccount('jhon doe',1000)
c1.deposit(50)
c1.withdraw(200)
c1.check_blance()
        