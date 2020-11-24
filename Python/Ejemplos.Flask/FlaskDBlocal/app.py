# --------------------------------------------------------------
#     EJEMPLO DE SERVICIO WEB CON FLASK - INTEGRA HTML Y CSS 
#     Base de datos local con SQL
#     Starting code para Laboratorio 7
# --------------------------------------------------------------
#   @Laura Arjona
#  @Sistemas Embebidos. 2020
# -----------------------------------

from flask import Flask, render_template, request, redirect,g,jsonify
#g is a special object that is unique for each request. 
#It is used to store data that might be accessed by multiple 
#functions during the request. The connection is stored and reused instead of 
#creating a new connection if get_db is called a second time in the same request.
import sqlite3
import json
import time
from random import randint
from datetime import datetime
    
DATABASE = 'db/database.db'

#instancia de la app de Flask
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# -----------------------------------------------
#  Consultar TODO el contenido de la tabla sensor
# -----------------------------------------------
def get_all_sensors(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM sensors")     
    sensors = cur.fetchall()
    return sensors

# -------------------------------------------------
#  Consultar las entradas de la tabla 'measurement'
#  cuyo valor de 'sensorid' sea igual a sensor_id
# --------------------------------------------------
def get_medidas(conn, sensor_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM measurements WHERE sensorid=" + sensor_id)     
    rows = cur.fetchall()
    measurements = []
    for row in rows:
        measurement = {}
        measurement['measurementid'] = row[0]
        measurement['unit'] = row[1]
        measurements.append(measurement)
    return measurements     

# --------------------------------------------------------------
#  Consultar TODAS las entradas de la tabla 'measurement-value'
# --------------------------------------------------------------
def get_medidas_valor(conn,medida_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM 'measurement-values' WHERE measurementid=" + medida_id)   
    medidas = cur.fetchall()
    return medidas


# ---------------------------
#  --------  ROUTING --------
# ---------------------------

# --------------------------------------------------------------
#  Menu principal --> 7templates/index.html
#  http://0.0.0.0:5000/index/
# --------------------------------------------------------------
@app.route("/index/")
def getIndex():  
    return render_template('index.html')
   
# --------------------------------------------------------------
#  Mostrar en el navegador el contenido de la tabla sensor
# http://0.0.0.0:5000/db/sensors/
# --------------------------------------------------------------
@app.route("/db/sensors/")
def getSensors():
    conn = get_db()
    sensors = get_all_sensors(conn)
    return render_template('db_sensor.html', data=sensors)
   
# --------------------------------------------------------------
#  Mostrar en el navegador los valores de las medidas con medidaid=medida_id
# Ejemplo para medidaid=6 (presión): http://0.0.0.0:5000/db/sensors/medidas/6/
# --------------------------------------------------------------
@app.route("/db/sensors/medidas/<medida_id>/")
def getMedidasValor(medida_id):
    conn = get_db()
    medidas_valor = get_medidas_valor(conn, medida_id)
    return render_template('db_medida_valor.html', data=medidas_valor)


# --------------------------------------------------------------
#  TODO: CONSULTAR LA TABLA DE LOS MOTORES
# la ruta debe ser: http://0.0.0.0:5000/db/motors
# --------------------------------------------------------------
@app.route("/db/motors")
def getMotores():
    # IMPLEMENTAR ESTA FUNCION
    return "DEBES MOSTRAR LA TABLA DE ESTADO DE LOS MOTORES AQUI :D "



# --------------------------------------------------------------
#  Dirección "home" -- registro de usuario
# http://0.0.0.0:5000/
# --------------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form
        username = req.get("username")
        email = req.get("email")
        password = req.get("password")

        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("sign_up.html", feedback=feedback)
        
        if username == "laura":
            #REDIRECCIONAMOS a la página del menu
            return redirect(f"/db/sensors/")
        else:
            #REDIRECCIONAMOS A LA route de home (/)
            return redirect(f"/")

    return render_template("sign_up.html")



#Es necesario incluir el host 0.0.0.0 para poder acceder al servicio
#desde fuera de la RPi donde estamos ejecutando este servicio
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
   
   
