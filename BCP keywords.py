#Break Statement:-
avi=5
info=int(input("Enter your data"))
i=1
while i<=info:
    if i>avi:
        break
    print("Hello")
    i+=1
#Continue Statement:-
for j in range(20):
    if j%3==0:
        continue
    else:
        print(j)
#Pass Statement:-
for k in range(1,21):
    if(k%2!=0):
        pass
    else:
     print(k)

