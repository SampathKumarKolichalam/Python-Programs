num1=int(input("Enter your number1:"))
num2=int(input("Enter your number2:"))
try:
    print("Division started")
    print(num1/num2)
except ZeroDivisionError  as error_description:
    print("Hey,you cannot divide any number with zero:",error_description)
except ValueError as error_description:
    print("Invalid Input:",error_description)
except Exception as error_description:
    print("Something went wrong",error_description)
finally:
    print("Division stopped")
