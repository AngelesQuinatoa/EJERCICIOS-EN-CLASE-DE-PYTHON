from socket import INADDR_UNSPEC_GROUP
from account import Account


class User(Account) :
    idUser     = int
    
    def __init__(self, name, document, email, password, gender, numberCell, age, idUser):
        super().__init__(name, document, email, password, gender, numberCell, age)
        self.idUser       = idUser 
        