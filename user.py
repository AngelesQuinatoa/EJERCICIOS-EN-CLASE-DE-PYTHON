from account import Account


class User(Account) :
    id     = int
    
    def __init__(self, name, document, email, password, gender, numberCell, age, id):
        super().__init__(name, document, email, password, gender, numberCell, age)
        self.id         =id