from flask import Flask, request, render_template
import pymssql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = "Hello world"
    sql_message=''
    
    if request.method == 'POST':
        sql_message = request.form.get('sql_message')
        sql_send(sql_message)
    return render_template("index.html", message=message, sql_message=sql_message)
def sql_connect():
    user = 'sa'
    password = 'yourStrong(!)Password'
    db = 'mito'
    host = '192.100.10.10'
 
    conn = pymssql.connect(host, user, password, db)
    return conn
def sql_send(sql_message):
    conn = sql_connect()
    cursor = conn.cursor()  
    cursor.execute("INSERT dbo.Messages (Message) OUTPUT INSERTED.id VALUES ('"+sql_message+"')")  
    row = cursor.fetchone()  
    while row:  
        print("Inserted Product ID : " +str(row[0]))
        row = cursor.fetchone()  
    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
