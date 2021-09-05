#Duck Typing:-
class vscode:
    def execute(self):
        print("debug")
        print("compile")
class  myeditor:
    def execute(self):
        print("share code")
        print("auto complete")
        print("debug")
        print("compile")
class laptop:
    def code(self,ide):
        ide.execute()
ide=myeditor()
lappy=laptop()
lappy.code(ide)
#Operator Overloading:-
class student:
    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
s1=student(70,80)
s2=student(80,90)
s3=s1+s2
print(s3.m1)
print(s3.m2)
#Method Overloading:-
class addition:
    def sum(self,a,b):
        add=a+b
        print(add)
    def sum(self,a=0,b=0,c=0):
        add=a+b+c
        print(add)
a=addition()
a.sum(2,2)
a.sum()
a.sum(2,2,2)
#Method OverRidding:-
class fathers_mobile:
    def mobile_company(self):
        print("Samsung galaxy")
class my_mobile(fathers_mobile):
    def mobile_company(self):
        print("Samsung galaxy A20'S ")
obj=my_mobile()
obj.mobile_company()
