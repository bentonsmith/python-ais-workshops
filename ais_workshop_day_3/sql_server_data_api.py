import pyodbc
from flask import Flask, g, render_template, abort, request
import json

# Globals
CONNECTION_STRING = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:usu-mis.database.windows.net,1433;Database=ais_workshop;Uid=mckelly@usu-mis;Pwd=USU-mis.ais;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'


# Setup Flask
app = Flask(__name__)
app.config.from_object(__name__)

# Before / Teardown
@app.before_request
def before_request():
    try:
        g.sql_conn =  pyodbc.connect(CONNECTION_STRING, autocommit=True)
    except Exception as e:
        abort(500, "No database connection could be established.")

@app.teardown_request
def teardown_request(exception):
    try:
        g.sql_conn.close()
    except AttributeError:
        pass

# CPI Help Page
@app.route('/', methods=['GET'])
def api_help():
    return render_template('cpi_api_help.html')

# GET All CPI
@app.route('/api/v1/cpi', methods=['GET'])
def get_cpi_data():
    curs = g.sql_conn.cursor()
    query = 'select top 1000 * from dbo.CPI_MKP_AIS'
    curs.execute(query)

    columns = [column[0] for column in curs.description]
    data = []

    for row in curs.fetchall():
        data.append(dict(zip(columns, row)))
    return json.dumps(data, indent=4, sort_keys=True, default=str)



# GET Single CPI
@app.route('/api/v1/cpi/<string:id>', methods=['GET'])
def get_single_cpi_data(id):
    curs = g.sql_conn.cursor()
    curs.execute("select * from dbo.CPI_MKP_AIS where id = ?", id)

    columns = [column[0] for column in curs.description]
    data = []

    for row in curs.fetchall():
        data.append(dict(zip(columns, row)))

    return json.dumps(data, indent=4, sort_keys=True, default=str)

# POST API (Add)
@app.route('/api/v1/cpi', methods=['POST'])
def insertnew():
    data = request.get_json()

    curs = g.sql_conn.cursor()

    query = 'insert dbo.CPI_MKP_AIS (CPIAUCSL,ObservationDate) VALUES (?,?)'

    if isinstance(data, dict):
        curs.execute(query, data["CPIAUCSL"], data["ObservationDate"])
        curs.commit()

    if isinstance(data, list):
        for row in data:
            curs.execute(query,row["CPIAUCSL"],row["ObservationDate"])
            curs.commit()

    return 'success', 200

@app.route('/api/v1/cpi/<string:id>', methods=['DELETE'])
def delete_single(id):
    curs = g.sql_conn.cursor()

    curs.execute("delete dbo.CPI_MKP_AIS where id = ? and CPIAUCSL < ?", id, 10)

    curs.commit()

    return 'success', 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")