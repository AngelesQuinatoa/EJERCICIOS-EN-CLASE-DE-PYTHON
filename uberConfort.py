import imp
from car import Car

class UberConfort(Car):
    numberPassanggers       = int
    carAccepted             = []
    seatMaterial            = []
    
    def __init__(self, license, driver, numberPassanggers, carAccepted, seatMaterial):
        super().__init__(license, driver)
        self.numberPassanggers      = numberPassanggers
        self.carAccepted            = carAccepted
        self.seatMaterial           = seatMaterial