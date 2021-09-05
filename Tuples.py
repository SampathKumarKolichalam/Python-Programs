"""info=("Sampath",19,38,"khammam")
print(info)
print(info[0])#Accesssing values using positive index numbers.
print(info[-4])#Accesssing values using negative index numbers.
print(len(info))#Accessing the length of string.
del info
print(info)"""
l1=("sam","ram","jam")
l2=(18,19,20)
l3=l1+l2 #joining two tuples
print(l3)
print(max(l1))#To get maximum value from tuple,but for strings ascii value of first letter of tuple items. 
print(min(l1))#To get minimum value from tuple,but for strings ascii value of first letter of tuple items.
#Directly we can't update tuple but,we can update using lists:-
fruit_tuple=("Apple","Orange","Mango")
print(fruit_tuple)
fruit_list=list(fruit_tuple)
fruit_list[2]="pineapple"
fruit_tuple=tuple(fruit_list)
print(fruit_tuple)