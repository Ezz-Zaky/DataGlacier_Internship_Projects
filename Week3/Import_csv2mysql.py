import pandas as pd
cabdata = pd.read_csv('City.csv', index_col=False, delimiter = ',')
cabdata.head()
import mysql.connector as msql
conn = msql.connect(host='localhost', user='root',password='0000')
cursor = conn.cursor()
cursor.execute("USE dg_week2;")
sql = "INSERT INTO city VALUES (%s,%s,%s)"
for i, row in cabdata.iterrows():
     cursor.execute(sql, tuple(row))
     print("Record inserted")
conn.commit()
print('Done importing')







