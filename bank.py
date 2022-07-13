from payment import Payment

class Bank(Payment):
    bank                = str
    identification      = str
    numberAccount       = int
    
    def __init__(self, id, ammouny, bank, identification, numberAccount):
        super().__init__(id, ammouny)
        self.bank           = bank
        self.identification = identification
        self.numberAccount  = numberAccount
    