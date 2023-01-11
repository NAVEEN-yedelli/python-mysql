import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',password='naveen@7386',database='deltax')
mycursor=mydb.cursor()

mycursor.execute("create table songs(Artist varchar(30) , DOB varchar(30),songname varchar(30) )")
myface=mycursor.fetchall()
for x in myface:
    print(x)