import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',password='naveen@7386',database='deltax')
mycursor=mydb.cursor()

insertedata="insert into songs(Artist,DOB,songname)value(%s,%s,%s)"

records=[
    ("Geetha Madhuri ","24 August 1989","Chirutha,Darlinge"),
    ("DeviSriPrasad","2August1979","Pakdo Pakdo , Ninnu Chudag"),
]
mycursor.executemany(insertedata,records)
mydb.commit()