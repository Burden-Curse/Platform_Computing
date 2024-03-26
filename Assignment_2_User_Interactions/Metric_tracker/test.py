import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Gerlie100",
    database="cse4500"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Measurements (TimeStamp VARCHAR(255), Presence Time INTEGER(10), Scrolling (Current Pixel) INTEGER(10), Title Name VARCHAR(255))")

#for db in mycursor:
#    print(db)

#mycursor.execute("CREATE TABLE Measurements (Timestamp VARCHAR(255), Presence Time FLOAT(10), Scrolling Pixel INTEGER(10), Title Name VARCHAR(255))")