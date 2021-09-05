#Without Parameters:-
def addition():
    a=1
    b=4
    c=a+b
    print(c)
addition()#Same for subtraction,multiplication,division but change in operators.
#Using parameters:-
def info(name,rollno):
  print(name)
  print(rollno)
info("Sampath","38")
#return type:-
def mul(x,y):
    return(x*y)
print(mul(3,4))
print(mul(4,4))
#Arbitary arguments(*):-Used when arguments are unknown * is used before argument name.
def fruits(*fruitlist):
    print(fruitlist[0])
    print(fruitlist[1])
    print(fruitlist[2])
    print(fruitlist[3])
fruits("orange","apple","grapes","pineapple")

#keyword variable length arguments:-
def person(n,**data):
 print(n)
 for i,j in data.items():
      print(i,j)
person("Sampath",age=19,city="khammmam")

#Recursion:-
def factorial(no):
    if no>1:
        return no* factorial(no-1)
    else:
        return 1
n=int(input("Enter any number"))
print("factorial is:",n,"is",factorial(n))

