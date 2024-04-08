import mysql.connector as sqltor
con1=sqltor.connect(host="localhost",user="root",password="")#con1 is the 1st connection 
cr1=con1.cursor() #cursor to check for presence of database
cr1.execute("show databases")
a="not in"
b=0
ch5=0
ud=["username","password","question","answer"]
c=["create table login(username varchar (10),password varchar(50),squest varchar(50),sans varchar(30))","create table questions(subj varchar(15),quest varchar(300),username varchar(10))","create table answers(subj varchar(15),quest varchar(300),ans varchar(550),username varchar(10))"]
sq=["place of birth","favourite colour","pets name"]
count=[]# for the tables
for x in cr1:#iterates through cursor that contains all the database name
    if "ip_project" in x:
        a='in'#if project is in changes 'a' to in
if a=="not in":
    cr1.execute("create database ip_project")#if not in creates database
con2=sqltor.connect(host="localhost",user="root",password="",database="ip_project")#connection to database ip_project 
cr2=con2.cursor()#cursor to check if table is in database
tabs=['login','questions','answers']#required table names
cr2.execute("show tables")#displays all the tables in particular database
for x in cr2:
    for y in tabs:#checks for presence of table
        if y in x:
            count.append(y)#adds tables name to an empty list if the table is present
for y in tabs:
    if y not in count:#checks if required table is present in database
        cr2.execute(c[b])#creates table 
    b=b+1
ch1=int(input("Enter 1 to log in or 2 to sign up:\n"))#ch1 holds choice
while ch1!=1 and ch1!=2:#to ensure that person has entered proper value of ch1
    print("Enter only 1 or 2")
    ch1=int(input("Enter 1 to log in or 2 to sign up:\n"))
if ch1==1:#login
    while 0!=-1:
        uname=input("Enter your username:\n")
        pw=input("Enter your password:\n")
        q1='select username,password from login where password="'+pw+'" and username="'+uname+'"'
        q2='select username,password from login where username="'+uname+'"'
        cr3=con2.cursor()#cursor for pw
        cr4=con2.cursor()#cursor for uname
        cr3.execute(q1)#execute for pw
        dis1=cr3.fetchall()#to get password
        cr4.execute(q2)#execute for uname
        dis2=cr4.fetchall()#to get username
        if dis1!=[] and dis2!=[] and pw in dis1[0] and uname in dis2[0]:
            ch3=0
            break
        else:
            if dis2==[] or uname not in dis2[0]:
                print("Entered username does not exist.")
                ch4=int(input("Do you want to sign up?\n1: yes\n2: no\n"))
                while ch4!=1 and ch4!=2:
                    ch4=int(input("Do you want to sign up?\n1: yes\n2: no\n"))
                if ch4==1:
                    ch1=2
                    break
                else:
                    continue
            if dis1==[] or pw not in dis1:
                print("Entered password is incorrect")
                ch3=int(input("Forgot password?\n1: yes\n2: no\n"))
                while ch3!=1 and ch3!=2:
                    ch3=int(input("Forgot password?\n1: yes\n2: no\n"))
                if ch3==1:
                    break
    if ch3==1:#enters only if username is valid
        while 0>-1:
            cr5=con2.cursor()
            q3='select squest from login where username="'+uname+'"'#squest contains confirmatory username
            cr5.execute(q3)#cursor for the above query
            dis3=cr5.fetchall()
            for z in sq:
                if z in dis3[0]:
                    print("What is your ",z,"?")
            sa=input("Enter the required answer:\n")
            cr6=con2.cursor()
            q4='select sans from login where username="'+uname+'"'#sans is the answer to confirmatory question
            cr6.execute(q4)
            dis4=cr6.fetchall()
            while sa.lower() not in dis4[0]:
               sa=input("Enter the required answer:")
            ch5=int(input("Do you want to reset your password?\n1: yes \n2: no\n"))
            while ch5!=1 and ch5!=2:
                ch5=int(input("Do you want to reset your password?\n1: yes\n2: no\n"))
            if ch5==1 or ch5==2:
                break
    if ch5==1:#if user wants to reset password
        pw=input("Enter a new password:\n")
        pw1=input("Confirm passwrord:\n")
        while pw!=pw1:
            print("Passwords dont match")
            pw=input("Enter a password:\n")
            pw1=input("Confirm passwrord:\n")
        cr7=con2.cursor()
        q4='update login set password="{}" where username="{}"'.format(pw,uname)  
        cr7.execute(q4)
        con2.commit()#change password and store it in pw then we use the commmit function
if ch1==2:
    uname=input("Enter a username:\n")
    w="not in"
    cr8=con2.cursor()
    q5="select username from login"
    cr8.execute(q5)
    dis5=cr8.fetchall()
    while 0>-1:
        w='not in'
        for x in dis5[0]:
            if uname in x:
                w="in"
        if w=="not in":
            break
        else:
            print("The username chosen is already taken")
            uname=input("Enter a username:\n")
    pw=input("Enter a password:\n")
    pw1=input("Confirm password:\n")
    while pw!=pw1:
        print("The passwords entered doesnt match")
        pw=input("Enter a password:\n")
        pw1=input("Confirm password:\n")
    print("Select a confirmation question:\n1: What is your place of birth?\n2: What is your favourite colour?\n3: What is your pets name?")
    chq=int(input("Enter a number from 1 to 3:\n"))
    while chq!=1 and chq!=2 and chq!=3:
        print("Enter only 1,2 or 3")
        chq=int(input("Enter a number from 1 to 3:\n"))
    sa=input("Enter an answer to the chosen question:\n")
    cr9=con2.cursor()
    q6='insert into login values("{}","{}","{}","{}")'.format(uname,pw,sq[chq-1],sa)
    cr9.execute(q6)
    con2.commit()
print("1: To answer a question,","\n2: To ask a question","\n3: To view profile")
ch2=int(input("Enter only 1 ,2 or 3:\n"))
while ch2!=1 and ch2!=2 and ch2!=3:
    print("1: To answer a question,","\n2: To ask a question","\n3: To view profile")
    ch2=int(input("Enter only 1 ,2 or 3:\n"))
while 0>-1:
    if ch2==1:#ans question
        print("Subjects:","\n 1:physics","\n 2:chemistry","\n 3:maths")
        chs=int(input("Which subject do you want to answer?"))
        while chs!=1 and chs!=2 and chs!=3:
            print("Enter only 1 or 2 or 3")
            chs=int(input("Which subject do you want to answer?\n"))
        slist={1:'phys',2:'chem',3:'math'}
        cr10a=con2.cursor()
        q7a='select q.quest from questions q,answers a where q.quest<>a.quest and q.subj="'+slist[chs]+'"'
        cr10a.execute(q7a)
        disq=cr10a.fetchone()
        if disq==[]:
            cr10b=con2.cursor()
            q7b='select q.quest from questions q,answers a where q.subj="'+slist[chs]+'" and q.username<>"'+uname+'"'
            disq=con2.fetchone()
        print("question: "+disq[0])
        ans=input("Type your answer:")
        #select statement using cursor that checks for answers="NULL"
        cr11=con2.cursor()
        print("4")
        q8='insert into answers values("{}","{}","{}","{}")'.format(slist[chs],disq,ans,uname)
        print("3")
        cr11.execute(q8)
        print("2")
        con2.commit()
        print("1")
    if ch2==2:
        print("Subjects:","\n 1:physics","\n 2:chemistry","\n 3:maths")
        chs=int(input("Which subject is your question from?"))
        while chs!=1 and chs!=2 and chs!=3:
            print("Enter only 1 or 2 or 3")
            print("Subjects","\n 1:physics","\n 2:chemistry","\n :.maths")
            chs=int(input("Which subject is your question from?\n"))
        ques=input("Type your question here:\n")
        cr12=con2.cursor()
        q9='insert into questions values("{}","{}","{}")'.format(slist[chs],ques,uname)
        cr12.execute(q9)
        con2.commit()
    if ch2==3:
        cr13=con2.cursor()
        q10='select * from login where username="'+uname+'"'
        cr13.execute(q10)
        dis11=cr13.fetchall()
        udcount=0
        for x in dis11[0]:
            print(ud[udcount],":\n",x)
            udcount=udcount+1
        cr14=con2.cursor()
        q11='select count(quest) from questions where username="'+uname+'"'
        cr14.execute(q11)
        dis12=cr14.fetchall()
        print("questions asked:\n",dis12[0])
        cr15=con2.cursor()
        q12='select count(ans) from answers where username="'+uname+'"'
        cr15.execute(q12)
        dis13=cr15.fetchall()
        print("questions answered:\n",dis13[0])
    print("Enter:","\n1: To answer a question,","\n2: To ask a question","\n3: To view profile,\n4: To quit")
    ch2=int(input("Enter only 1,2,3 or 4\n"))
    while ch2!=1 and ch2!=2 and ch2!=3 and ch2!=4:
        print("Enter:","\n1: To answer a question,","\n2: To ask a question","\n3: To view profile,\n4: To quit")
        ch2=int(input("Enter only 1,2,3 or 4\n"))
    if ch2==4:
        break
