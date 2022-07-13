from codecs import getencoder
from curses import ACS_GEQUAL
import mailbox
from unicodedata import name
class Account:
    id          = int
    name        = str
    document    = int
    email       = str
    password    = str
    gender      = str
    numberCell  = int
    age         = int
    
    #Metodo constructor en Python
    def __init__(self, name, document, email, password, gender, numberCell, age):
        self.name       = name
        self.document   = document 
        self.email      = email
        self.password   = password
        self.gender     = gender
        self.numberCell = numberCell
        self.age        = age
        
        