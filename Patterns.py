"""
####
####
####
####
"""
#Printing  above pattern:-
for i in range(4):
    for j in range(4):
     print("#",end="")
    print()
"""
#
##
###
####
"""
#Printing  above pattern:-
for i in range(4):
    for j in range(i+1):
     print("#",end="")
    print()
"""
####
###
##
#
"""
#Printing  above pattern:-
for i in range(4):
    for j in range(4-i):
     print("#",end="")
    print()
""""
* 
* *
* * *
* * * *"""
#Printing  above pattern:-
n=int(input("Enter any number"))
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))