import email


class Account:
    id          = int
    name        = str
    document    = str
    email       = str
    password    = str
    gender      = str
    numberCell  = int
    age         = int
    
    
    #Metodo constructor en Python
    def __init__(self, name, document):
        self.name       = name
        self.document   = document 
        
        