import sqlite3

## connect to sqlite
connection=sqlite3.connect("student.db")

## create  a cursor object ti insert record,create table and retrieve
cursor=connection.cursor()

## create the table

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)
## insert some more records

cursor.execute('''Insert into STUDENT values('varsha','DataScience','A',90)''')
cursor.execute('''Insert into STUDENT values('aishwarya','DataScience','B',100)''')
cursor.execute('''Insert into STUDENT values('sowjanya','DataScience','A',86)''')
cursor.execute('''Insert into STUDENT values('surya','DEVOPS','A',50)''')
cursor.execute('''Insert into STUDENT values('suresh','DEVOPS','A',35)''')
## Display all the records

print("The Inserted records are")
data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

## close the connection

connection.commit()
connection.close()