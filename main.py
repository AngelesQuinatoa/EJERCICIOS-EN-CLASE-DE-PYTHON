from cgi import print_form
from lib2to3.pgen2 import driver
from pprint import pprint
from tkinter import RADIOBUTTON
from account import Account
from car import Car
from driver import Driver
from payment import Payment
from route import Route
from user import User

if __name__ == "__main__":
    print("Hola mundo")
    
    carro = Car()
    carro.id           = 5
    carro.brand        = "Toyota"
    carro.driver       = "Angeles"
    carro.passanggers  = 11
    
    print(vars(carro))
    
    carro2 = Car()
    carro.id           = 2
    carro.brand        = "Toyota"
    carro.driver       = "Angeles"
    carro.passanggers  = 11
    
    print(vars(carro)) 
    print(vars(carro2))
    
    
    cuenta = Account()
    cuenta.id          = 3
    cuenta.name        = "Alexis"
    cuenta.document    = 1752290906
    cuenta.email       = "nagelyquinatoa3@gmail.com"
    cuenta.password    = "alexisn"
    
    print(vars(cuenta))
    
    pago = Payment()
    pago.id          = 4
    pago.ammouny     = 45
    
    print(vars(pago))
    
    ruta = Route()
    ruta.id       = 567
    ruta.start    = "Magdalena"
    ruta.end      = "Chillogallo"
    
    print(vars(ruta))
    
    usuario = User()
    usuario.id      = 45678
    usuario.nombre  = "Alexis"
    usuario.apellido    = "Quinatoa"
    
    print(vars(usuario))
    
    conductor = Driver()
    conductor.id        = 8
    conductor.name      = "Mateo"
    conductor.document  = 1717758268
    conductor.email     = "mateo@gmail.com"
    conductor.password  = "Mateo1234"
    
    print(vars(conductor))

