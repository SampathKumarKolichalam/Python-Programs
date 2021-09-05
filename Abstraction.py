#Example:-1
from abc import ABC,abstractmethod
class Mobile(ABC):
    @abstractmethod
    def calling(self):
        pass
class Telephone(Mobile):
     def calling(self):
         print("we can call using telephone")
#obj1=Mobile()
#obj1.calling()
obj2=Telephone()
obj2.calling()
#Example:-2
from abc import ABC,abstractmethod
class car_hide(ABC):
    @abstractmethod
    def piston(self):
        pass
    @abstractmethod
    def inventor(self):
       pass
    def oiltype(self):
        print("Petrol is used")
class car_unhide(car_hide):
    def company(self):
        print("Tata Nexon")
    def price(self):
        print("7.5 Lakh")
    def color(self):
        print("Blue")
obj=car_unhide()
obj.company()
obj.oiltype()
