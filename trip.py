from car import Car
from driver import Driver
from payment import Payment
from user import User
from rute import Rute


class Trip(Car, Payment, User, Rute, Driver):
    idTrip         = int
    
    def __init__(self, idTrip, idUser, idDriver, star, end, kmDistance, typePayment, ammount, date, licence, driver ):
        super().__init__(idTrip, idUser, idDriver, star, end, kmDistance, typePayment, ammount, date, licence, driver)
        self.idTrip     = idTrip