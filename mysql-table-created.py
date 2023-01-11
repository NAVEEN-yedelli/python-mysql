import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',password='naveen@7386',database='deltax')
mycursor=mydb.cursor()

mycursor.execute("show tables ")
for x in mycursor:
    print(x)