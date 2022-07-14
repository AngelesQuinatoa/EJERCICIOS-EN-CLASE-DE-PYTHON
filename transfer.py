from multiprocessing.spawn import import_main_path
from payment import Payment
from bank import Bank

class Transfer(Bank):
    
    def __init__(self, id, ammount, date, bankName, identification, numberAccount, typePayment):
        super().__init__(id, ammount, date, bankName, identification, numberAccount, typePayment )