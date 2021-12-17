from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'empleados'
app.config['SECRET_KEY'] = 'codoacodo' # Seteo de cookie

mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()
    
    sql = "select * from empleados"
    
    cursor.execute(sql)
    conn.commit()
    
    return render_template('empleados/index.html')
    
if __name__ == '__main__':
    app.run(debug=True)