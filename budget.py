class Category:

    def __init__(self, category):
        self.name = category
        self.ledger = []

    def deposit(self, amount, description=''):
        deposit = {'amount': amount, "description": description}
        self.ledger.append(deposit)

    def withdraw(self, amount, description=''):
        if self.check_funds(-amount):
            withdraw = {'amount': -amount, "description": description}
            self.ledger.append(withdraw)
            return True
        else:
            return False
        
    def get_balance(self):
        self.ledger[0]['amount'] += amount
        print(self.ledger)
        return self.ledger[0]['amount']

    def check_funds(self, amount):
        amount >= self.get_balance(amount)
        return True