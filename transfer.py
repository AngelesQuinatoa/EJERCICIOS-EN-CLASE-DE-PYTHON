from multiprocessing.spawn import import_main_path
from payment import Payment
from bank import Bank

class Transfer(Payment, Bank):
    
    def __init__(self, id, ammouny, bank, identification, numberAcoount):
        super().__init__(id, ammouny, bank, identification, numberAcoount)