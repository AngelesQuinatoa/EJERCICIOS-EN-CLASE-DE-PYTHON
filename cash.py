from payment import Payment

class Cash(Payment):
    
    def __init__(self, id, ammouny,typePayment):
        super().__init__(id, ammouny, typePayment)