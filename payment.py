from datetime import date


class Payment :
    id                  =int
    ammouny             =int
    date                =str
    typePayment         =[]
    
    def __init__(self, id, ammouny, typePayment):
        self.id         = id
        self.ammouny    = ammouny
        self.date       = date
        self.typePayment    = typePayment