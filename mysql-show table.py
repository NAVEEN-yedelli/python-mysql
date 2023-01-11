import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',password='naveen@7386',database='deltax')
mycursor=mydb.cursor()


mycursor.execute("select * from songs ")
result=mycursor.fetchall()
for row in result:
    print(row)
