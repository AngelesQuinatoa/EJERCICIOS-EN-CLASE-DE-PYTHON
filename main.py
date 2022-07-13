from account import Account
from car import Car

if __name__ == "__main__":
    print("Hola mundo")
    
    car = Car("PBO5555", Account("Angeles Quinatoa", "1717758260"))
    print(vars(car))
    print(vars(car.driver))

