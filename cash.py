from payment import Payment

class Cash(Payment):
    
    def __init__(self, id, ammouny,):
        super().__init__(id, ammouny)