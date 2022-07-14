from payment import Payment

class Bank(Payment):
    bank                = str
    identification      = str
    numberAccount       = int
    
    def __init__(self, id, typePayment, ammouny, date, bank, identification, numberAccount):
        super().__init__(id, typePayment, ammouny, date)
        self.bank           = bank
        self.identification = identification
        self.numberAccount  = numberAccount
    