import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   #      LAST_NAME, AGE, SEX, INCOME)
       #  VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
