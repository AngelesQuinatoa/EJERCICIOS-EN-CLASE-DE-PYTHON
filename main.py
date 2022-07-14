from account import Account
from car import Car
from uberX import UberX

if __name__ == "__main__":
    
    car = Car("PBO5555", Account("Angeles Quinatoa", "1717758260"))
    print(vars(car))
    print(vars(car.driver))
    
    
    uberX = UberX("PCC-12345", Account("Angeles", "555555555"), "Chevrolet", "Spark")
    print(vars(uberX))

