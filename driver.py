from account import Account

class Driver :
    id          = int
    license     = str
    
    
    def __init__(self, id, license, name, document, email, password, gender, numberCell, age):
        super().__init__(name, document, email, password, gender, numberCell, age)
        self.id         = id
        self.license    = license