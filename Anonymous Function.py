#Lamba Function:-
#Example 1:-
x=lambda a,b:a-b
print(x(10,5))
#Example 2:-
squ=lambda x:x*x
print(squ(5))
#Example 3:-
def squa(y):
    return lambda x:x*y
resu=squa(7)
print(resu(5))
#Other functions used with this anonymous function:-
# filter() function:-
nums_list=[1,2,3,4,5,6,7,8,9,10]
odd_num=list(filter(lambda n:n%2!=0,nums_list))#Finding odd numbers from nums_list.
even_num=list(filter(lambda n:n%2==0,nums_list))#Finding even numbers from nums_list.
print("All Numbers in list:",nums_list)
print("Odd Numbers in list:",odd_num)
print("Even Numbers in list:",even_num)
# map() function:-
num_list=[1,2,3,4,5,6,7,8,9,10]
num_squarelist=list(map(lambda a:a*a,num_list))#Squaring the numbers of the list.
print("All Numbers in list:",num_list)
print("squares of the numbers in list:",num_squarelist)
# reduce() function:-
from functools import reduce
numb_list=[1,2,3,4,5,6,7,8,9,10]
sum_list=reduce(lambda a,b:a+b,numb_list)
print("All Numbers in list:",numb_list)
print("Sum of all the numbers in a list:",sum_list)