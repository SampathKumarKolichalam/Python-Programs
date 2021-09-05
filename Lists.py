"""info=[38,9.33,"Sampath"]
print(info)
print(info[2])#Accessing values of list using positive index numbers.
print(info[-1])#Accessing values of list using negative index numbers.
print(type(info))#To get the datatype of variable,type() is used.
info[1]=9.35#Updating values in a list.
print(info)
print(len(info))#To get the length of a list.
info.append(19)#To add values/items into a list.
info.insert(3,"Khammam")#To add values/items into a list at a particular index.
print(info)
info.remove(9.35)#To remove/delete values in a list.
info.pop()# To remove/delete values in lifo/filo order.
print(info)
del info#To delete full list.
print(info)"""
l1=["sam","ram","jam"]
l2=["kumar",18,38]
l3=l1+l2#To join two lists.
print(l3)
print(max(l1))#To get maximum value from list,but for strings ascii value of first letter of list items. 
print(min(l1))#To get minimum value from list,but for strings ascii value of first letter of list items.
l1.reverse()#To reverse the list.
print(l1)
l1.sort()# To sort the list.
print(l1)