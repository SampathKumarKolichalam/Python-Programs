#Private Methods:-
class encap:
    def __init__(self) -> None:
        self.__priv_fun()#To call private method outside class using __init__ method.
    def pub_fun(self):
        print("It is Public function,we access it anywhere in the program")
    def __priv_fun(self):
        print("It is Private function,we access it inside the class only")
enobj=encap()
enobj.pub_fun()
#enobj.__priv_fun()
#private Variables:-
class abc:
    __a=0
    __b=0
    def __init__(self) -> None:
        self.__a=10
        self.__b=20
    def show_var(self):
        print(self.__a+self.__b)
obj=abc()
obj.show_var()
obj.__a=100

