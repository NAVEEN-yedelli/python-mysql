import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',password='naveen@7386',)
mycursor=mydb.cursor()

mycursor.execute("create database deltax")