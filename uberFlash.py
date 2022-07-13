from car import Car

class UberFlash(Car):
    brand       =str
    model       =str
    loadSize    =[]
    loadWeight  =int
    
    def __init__(self, license, driver, brand, model, loadSize, loadWeight):
        super().__init__(license, driver)
        self.brand      = brand
        self.model      = model
        self.loadSize   = loadSize
        self.loadWeight = loadWeight