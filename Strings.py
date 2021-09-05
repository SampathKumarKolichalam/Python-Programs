name="Sampath"
print(name)
print(name[0])#index value
print(name[-7])
print(name[6])
print(name[-1])
data="I Love python"
print(data)
print(data[2:7])#range from one character to some particular character.
print(data[7:13])#range from one character to some particular character.
print(data[2:])#range from one character to last character of string.
info="""Hi!Welcome to simplest
python programming"""#Multi Line String.
print(info)
str1="Sampath Kumar"
str2=" Kolichalam"
str3=str1+str2#string concatenation.
print(str3)
# String Methods:-
book="xyz"
price=300
details="The price of book '{}' is Rs:{}".format(book,price)#To add numbers and strings values format() method is used.
print(details)
py="Python"
print(py*5)#String Repetation.
strs="Sampath Kumar"
print(strs.capitalize())#Converts first letter of string into uppercase.
print(strs.casefold())#Converts total string into lowercase.
print(strs.center(22))#Used to align the string into center as per our need.
print(strs.endswith("kumar"))#It returns true or false if it satisfys the condition.
print(strs.endswith("Kumar"))#It returns true or false if it satisfys the condition.
print(strs.startswith("Sampath"))#It returns true or false if it satisfys the condition.
print(strs.startswith("sampath"))#It returns true or false if it satisfys the condition.
print(strs.find("Kumar"))#Used to search the Specified string starting index number in a string.
strings1="sampath"
strings2="38"
strings3="ab@cd"
strings4="kumar123"
print(strings1.isalpha())#Used to check the string is alphabetic or not.
print(strings2.isalpha())#Used to check the string is alphabetic or not.
print(strings1.isalnum())#Used to check the string is alphanumeric or not.
print(strings2.isalnum())#Used to check the string is alphanumeric or not.
print(strings1.isdecimal())#Used to check the string is decimal or not.
print(strings2.isdecimal())#Used to check the string is decimal or not.
print(strings1.isdigit())#Used to check the string is decimal or not.
print(strings2.isdigit())#Used to check the string is decimal or not.
print(strings1.isidentifier())#Used to check the string is identifier or not.
print(strings2.isidentifier())#Used to check the string is identifier or not.
print(strings3.isidentifier())#Used to check the string is identifier or not.
print(strings4.isidentifier())#Used to check the string is identifier or not.
stri1="Sampath"
stri2="kUMAR"
print(stri1.isspace())#Returns true string is  having white spaces,otherwise false.
print(stri2.isspace())#Returns true string is  having white spaces,otherwise false.
print(len(stri1))#length of string.
print(stri1.swapcase())#It converts lowercase characters into uppercase characters and viceversa.
print(stri2.swapcase())#It converts lowercase characters into uppercase characters and viceversa.
strss="I Love Python"
print(strss)
mylist=strss.split()#It is used to break the string into list. 
print(mylist)

