from abc import ABC, abstractmethod
class Parent:
    def Home(self):
        print("Parents home")

    def car(self):
        print("parents car")

    def money(self):
        pass    

class child(Parent):
    def money(self):
        print("child earns money")          

c=child()
c.Home()
c.car()
c.money()    