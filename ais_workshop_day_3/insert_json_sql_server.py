# Reading / Inserting JSON Data
import pyodbc
import json

connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:usu-mis.database.windows.net,1433;Database=ais_workshop;Uid=mckelly@usu-mis;Pwd=USU-mis.ais;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = pyodbc.connect(connection_string,autocommit=True) # autocommit = True, since it is the SQL Server way

curs = conn.cursor()

curs.execute(
     '''
     create table MKP_AIS_JSON(
     ID int primary key clustered identity(1,1)
     ,Title varchar(1000)
     ,Domain varchar(1000)
     )

   '''
)



insert_query = 'insert into MKP_AIS_JSON (Title, Domain) values (?,?)'
with open(r'd:\usu\ais_workshop\ais_workshop_3\data\todayilearned.json') as data_file:
    data = json.load(data_file)
    data_list = data['data']['children']
    rows_to_insert = []
    for entry in data_list:
        rows_to_insert.append(tuple([entry['data']['title'], entry['data']['domain']]))
    curs.executemany(insert_query, rows_to_insert)




# Commit and close the connection
conn.commit()
conn.close()
