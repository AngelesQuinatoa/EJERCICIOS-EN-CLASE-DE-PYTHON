class Account:
    id          = int
    name        = str
    document    = str
    email       = str
    password    = str
    gender      = str
    numberCell  = int
    
    
    #Metodo constructor en Python
    def __init__(self, name, document, email, password, gender, numberCell, age):
        self.name       = name
        self.document   = document 
        self.email      = email
        self.password   = password
        self.gender     = gender
        self.numberCell = numberCell
        
        
        