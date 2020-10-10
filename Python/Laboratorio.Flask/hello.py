from flask import Flask
app = Flask(__name__)

@app.route('/valor')
def hello_world():
    return 'Hola, World!'