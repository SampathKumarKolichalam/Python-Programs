#Cricket Knowledge Quiz:-
que1="""" Which Second indian Cricketer Scored 6 sixes in a over in international cricket?
a.Yuvaraj Singh
b.Ravi Shastri
c.Rishab pant
d.MS Dhoni"""
que2="""" Which indian Cricketer took hat-trick in  icc odi world cup 2019?
a.J Bumrah
b.Bhuvi
c.M Shami
d.Virat Kohli"""
que3="""" In which year indian cricket team Won thier Second icc odi world cup?
a.2007
b.2013
c.1983
d.2011"""
questions={que1:"a",que2:"c",que3:"d"}
name=input("Enter Your Name:")
Score=0
print("Hello",name,"Welcome to Cricket Knowledge Quiz!!!")
for i in questions:
    print(i)
    ans=input("Enter Your Option:")
    if ans.lower()==questions[i]:
        print("Correct Answer,You got one point!")
        Score=Score+1
    else:
      print("Wrong answer,You lost one point!")
      Score=Score-1
print("Your final Score is:",Score)  