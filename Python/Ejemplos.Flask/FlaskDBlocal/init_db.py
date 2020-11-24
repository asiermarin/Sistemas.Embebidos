#  @Sistemas Embebidos. 2020
#  Inicialización de la base de datos SQL
# -----------------------------------

from flask import Flask, g
#g is a special object that is unique for each request. 
#It is used to store data that might be accessed by multiple 
#functions during the request. The connection is stored and reused instead of 
#creating a new connection if get_db is called a second time in the same request.
import sqlite3

    
DATABASE = 'db/database.db'

#instancia de la app de Flask
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('db/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        
        
init_db()