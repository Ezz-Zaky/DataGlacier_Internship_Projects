
import MySQLdb
mydb = MySQLdb.connect(host='127.0.0.1', user='root', password='', database='dg_week2')
with open('Cab_Data.csv') as cab:
    cabfile = csv.reader(cab, delimiter=',')
    cab_values = []
    for row in cabfile:
        value = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
        cab_values.append(value)
query='INSERT INTO cab_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
mycursor = mydb.connect()
mycursor.executemany(query, cab_values)
mydb.commit()