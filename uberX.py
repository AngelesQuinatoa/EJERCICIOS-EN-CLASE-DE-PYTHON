from io import BufferedRandom
from pyexpat import model
from car import Car


class UberX(Car):
    brand   = str
    model   = str
    
    def __init__(self, license, driver, broad, model):
        super().__init__(license, driver)
        self.brand = broad 
        self.model = model
        
    