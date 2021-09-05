#While Loop:-
#increment
i=1
while i<=5:
 print("Hello Sampath")
 i=i+1 
 #Decrement
 j=5
 while j>=1:
     print("Hello Python")
     j=j-1
#With Strings
inf0="Sampath"
k=0
while k<len(inf0):
    print(inf0[k])
    k=k+1
 #Nested While loops:-
i="Sampath"
j=1
while j<8:
    for x in i:
        print(j,x)
        j=j+1
        if x=="h":
            break  
#For Loop:-
x=["Sampath",19,38]#List
for i in x:
     print(i)
y='Sampath'#String
for j in y:
    print(j)
for k in range(10,20,2):#Range Function
 print(k)
num=int(input("Enter any Number:"))#Print Table of  any number
for l in range(0,11):
    print(num,"*",l,"=",num*l)
