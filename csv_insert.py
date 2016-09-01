import sqlite3
import csv
import os

#test members.csv
with open('members.csv',newline="",encoding='utf-8') as fin:
    csv_reader = csv.DictReader(fin)
    members = [(row['名字'],row['團體']) for row in csv_reader]
print(members)

#read sql file
with open('create_db.sql',encoding='utf-8') as fin:
    create_db_sql = fin.read()

#create connect session and using sql fite create table
db = sqlite3.connect('members.db')
with db:
    db.executescript(create_db_sql)


#insert into csv data
with db:
    db.executemany(
        "insert into members(name,group_name) values (?,?)",
         members
    )
#test sqlite db
c  = db.execute('select * from members ')
for row in c:
    print(row)
