class Payment:

    initial_balance = 1000

    def __init__ (self, recipient, amount):
        self.recipient = recipient
        self.amount = amount

    def check_balance(self):
        return Payment.initial_balance - self.amount
    
    @classmethod
    def update_initial_balance(cls, new_balance):
        cls.initial_balance = new_balance

    @staticmethod
    def validate_payment(time):
        if time >=8 and time <= 17 :
            return True
        else:
            return False
    
transanction = Payment("Chatheriyan", 200)
print(transanction.validate_payment(9))