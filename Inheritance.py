#Single inheritance:-
class parent:
    def func1(self):
        print("this is parent class")
class child(parent):
    def func2(self):
        print("this is child class")
ch=child()
ch.func2()
ch.func1()   
#Multilevel inheritance:-
class parent:
    def func1(self):
        print("this is parent class")
class child(parent):
    def func2(self):
        print("this is child class")
class grandchild(child):
    def func3(self):
        print("this is grandchild class")               
ch=grandchild()
ch.func3()
ch.func2()
ch.func1() 
#Hierarchical inheritance:-
class parent:
    def func1(self):
        print("this is parent class")
class child1(parent):
    def func2(self):
        print("this is child1 class")
class child2(parent):
    def func3(self):
        print("this is child2 class")               
ch=child2()
ch.func1()
ch.func2()
#Multiple inheritance:-
class Father:
    def func1(self):
        print("this is Father class")
class Mother:
    def func2(self):
        print("this is Mother class")
class child(Father,Mother):
    def func3(self):
        print("this is child class")
ch=child()
ch.func1()
ch.func2()
#Constructor in inheritance:-
class A:
    def __init__(self) -> None:
        print("this is class a init")
    def func1(self):
        print("this is func1 method")
class B(A):
    def __init__(self) -> None:
        print("this is class b init")
        super().__init__()
    def func2(self):
        print("this is func2 method")
obj=B()
#Method Resolution order(MRO):-left to right
class A:
    def __init__(self) -> None:
        print("this is class a init")
    def func1(self):
        print("this is func1_A method")
class B:
    def __init__(self) -> None:
        print("this is class b init")
    def func1(self):
        print("this is func2_B method")
class C(A,B):
    def __init__(self) -> None:
        print("this is class c init")
        super().__init__()
    def func3(self):
        print("this is func3 method")
    def func(self):
        super().func1()
obj=C()
obj.func1()
obj.func()




           


        