#__init__ Method:-Method 1(Parametrized Constructor with Additional Method)
class mobile:
    def __init__(self,ram,brand,price) -> None:
        self.ram=ram
        self.brand=brand
        self.price=price
        pass
    def showinfo(self):
        print(self.ram)
        print(self.brand)
        print(self.price)
obj=mobile('8GB','OnePlus','45000')
obj.showinfo()       
#__init__ Method:-Method 2(Parameterized Constructor without Additional Method)
class student:
    def __init__(self,name,rollno) -> None:
     print(name)
     print(rollno)
stu1=student("Sampath",38)
#__init__ Method:-Method 2(Non-Parameterized Constructor With Additional Method)  
class laptop:
    def __init__(self) -> None:
        print(" I am Non-Parametrized __init__ Method")
    def info(self):
        print("RAM:4GB")
        print("Price:70000")
        print("Company:Dell")
lappy=laptop()
lappy.info()

        
       

        