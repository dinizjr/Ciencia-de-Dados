import pymssql as bd
import pandas as pd
import pyodbc as pydb


cs = (
    "DRIVER={SQL Server};"
    "SERVER=177.159.191.123;"
    "UID=splmtv_admin;"
    "PWD='0admin0;'"
    )
print(cs)
cnxn = pydb.connect(cs)
print("Connected.")
cnxn.close()



#dsn="DRIVER={SQL SERVER};server=177.159.191.123;database=0714503_Radar;uid=splmtv_admin;pwd=0admin0"


'''
server_name = "177.159.191.123"
db_name = "0714503_Radar"

server = "Server="+str(server_name)
db = "Database="+str(db_name)
key = "Driver={SQL Server Native Client 11.0};"+server+";"+db+";"+"Trusted_Connection=yes;"

cnxn = pydb.connect(key)
'''


'''driver = '{SQL Server Native Client 11.0}'
cnxn = pydb.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 11 for SQL Server}',
    Server='177.159.191.123',
    Database='0714503_Radar'
)'''


'''
server = '{177.159.191.123}'
db = '{0714503_Radar}'
con = pydb.connect('Driver={SQL Server};SERVER=' + server + ';DATABASE=' + db)
query = '{select * from tbl_eqp}'
df = pd.read_sql(query,con)
print(df)
'''


'''conn = bd.connect(server="177.159.191.123", user="splmtv_admin", password="0admin0", database="0714503_Radar")

stmt = "select * from tbl_eqp"
df = pd.read_sql(stmt)
print(df)'''

'''conn = bd.connect(server="177.159.191.123", user="splmtv_admin", password="0admin0", database="0714503_Radar")
sursor = conn.cursor()
sql = "select * from tbl_eqp"
cursor.execute(sql)
results = cursor.fetchall()
for row in sql:
    print(row)'''

'''conn = bd.connect(server="177.159.191.123", user="splmtv_admin", password="0admin0", database="0714503_Radar")
cur = conn.cursor()
cur.execute("select * from tbl_eqp")
conn.commit()
row = cur.fetchone()
while row:
    print(conn)
conn.close()'''