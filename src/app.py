from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from pymysql.cursors import DictCursor
from flaskext.mysql import MySQL
from datetime import datetime

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'empleados'
app.config['SECRET_KEY'] = 'codoacodo' # Seteo de cookie

mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor(cursor=DictCursor)

def queryMySql(query, data = (), tipoDeRetorno = 'none'):
    if data != None:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
        
    if tipoDeRetorno == "one":
        registro = cursor.fetchone()
    else:
        registro = cursor.fetchall()
    
    if query.casefold().find("select") != -1:
        conn.commit()
    
    return registro

@app.route('/')
def index():  
    sql = "SELECT * FROM empleados;"
    empleados = queryMySql(sql, None,"all")
    
    conn.commit()

    return render_template('empleados/index.html', empleados=empleados)

@app.route('/empleado/alta', methods=["GET", "POST"])
def alta_empleado():
    if request.method == "GET":
        return render_template('empleados/create.html')
    elif request.method == "POST":
        _nombre = request.form['txtNombre']
        _correo = request.form['txtCorreo']
        _foto = request.files['txtFoto']
        
        if _nombre == '' or _correo == '':
            flash('El nombre y el correo son obligatorios.')
            return redirect(url_for('alta_empleado'))
        
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        
        if _foto.filename != '':
            nuevoNombreFoto = tiempo + '_' + _foto.filename
            _foto.save("src/uploads/" + nuevoNombreFoto)
        else:
            flash('La foto es obligatoria.')
            return redirect(url_for('alta_empleado'))
        
        sql = "INSERT INTO empleados (nombre, correo, foto) values (%s, %s, %s);"
        datos = (_nombre, _correo, nuevoNombreFoto)
        queryMySql(sql, datos)
        
        return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)