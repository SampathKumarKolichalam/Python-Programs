#Program to check number is prime number or not:-
no=int(input("Enter your number:"))
for i in range(2,no):
    if no%i==0:
        print("Not a prime  number!!!")
        break
else:
    print("Prime number!!!")