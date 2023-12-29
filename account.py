# The __init__ method is used to initialize the attributes of the object. It is the constructor method because it is invoked automatically when an object is instantiated. It is a constructor 
class Account: 
    def __init__(self):
        self.transactions = []
    def deposit(self, amount):
        trasaction = ('deposit', amount)
        self.transactions.append(trasaction)
    def withdraw(self, amount):
        trasaction = ('withdraw', amount)
        self.transactions.append(trasaction)
    def balance(self):
        total = 0
        for type, amount in self.transactions:
            if type == 'deposit':
                total += amount
                print('deposit')
            if type == 'withdraw':
                total -= amount
                print('withdraw')
        return(total)
    def __repr__(self):
        return '<Account: {}>'. format(len(self.transactions))
     