from account import Account

class Driver(Account):
    idDriver         = int
    license          = str
    
    
    def __init__(self, idDriver, license, name, document, email, password, gender, numberCell, age):
        super().__init__(name, document, email, password, gender, numberCell, age)
        self.idDriver         = idDriver
        self.license          = license