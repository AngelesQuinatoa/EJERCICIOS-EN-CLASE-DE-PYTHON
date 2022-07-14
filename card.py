from bank import Bank

class Card(Bank):
    cardNumber          = int
    cardSecurityCode    = int
    cardDate            = int
    
    def __init__(self, id, typePayment, ammouny, date, bank, identification, numberAccount, cardNumber, cardSecurityCode, cardDate):
        super().__init__(id, typePayment,  ammouny, date, bank, identification, numberAccount)
        self.cardNumber         = cardNumber
        self.cardSecurityCode   = cardSecurityCode
        self.cardDate           = cardDate
    