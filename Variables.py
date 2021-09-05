#In python no need to give datatype like int,float,char,string to variables,it will automatically assign data type to variables when we create a variables.
name="Sampath"
age=19
rollno=38
print(name)
print(age)
print(rollno)
#printing all above variables in one line:-
print(name,age,rollno)
#Assigning Single value to Multiple variables:-
a=b=c=100
print(a)
print(b)
print(c)
#Assigning Multiple values to Multiple Variables:-
x,y,z=10,20,30
print(x)
print(y)
print(z)
#Local Variables:-Variables can't access outside the function.
def add():
 p=20
 q=20
 print(p+q)
add()
# Global Variables:-variables can access anywhere in the function.
num_1=30
num_2=20
def sub():
    print("subtraction inside function:",num_1-num_2)
sub()
print("subtraction outside function:",num_1-num_2)
#Global Keyword:-
num=35
def shows():
  global num
  num=40
  print("inside function",num)
shows()
print("Outside function",num)
