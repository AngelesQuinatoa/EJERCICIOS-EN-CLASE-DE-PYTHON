

from car import Car
from driver import Driver
from payment import Payment
from account import Account
from rute import Rute


class Trip(Car, Payment, Account, Rute, Driver):
    idTrip         = int
    
    def __init__(self, license, driver, idUser, idDriver, idTrip, star, end, kmDistance, typePayment, ammount, date):
        super().__init__(self, license, driver, idUser, idDriver, idTrip, star, end, kmDistance, typePayment, ammount, date )
        self.idTrip             = idTrip