import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',password='naveen@7386',database='song')
mycursor=mydb.cursor()


r=input("enter name to delete \n")

sql="delete  from song123 where artist=%s"
add=[r]

mycursor.execute(sql,add)
mydb.commit()
print(mycursor.rowcount,"DELECTED SUCCESSFULL")