import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',password='naveen@7386',database='deltax')
mycursor=mydb.cursor()


r=input("enter Artist name \n")
s=input("enter Dob of Artist \n")
t=input("enter song name \n")

insertdata="insert into songs value(%s,%s,%s)"
records=(r,s,t)
mycursor.execute(insertdata,records)
mydb.commit()