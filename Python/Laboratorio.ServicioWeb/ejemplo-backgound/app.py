import threading
import atexit
from flask import Flask, render_template, request
from flask import request, redirect

import random

POOL_TIME = 5 #Seconds
GENES_POSIBLES = ' abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890,.-;:_¿?¡!'

ledSts = None
sensLuzSts = None

# variables that are accessible from anywhere
commonDataStruct = {}
# lock to control access to variable
dataLock = threading.Lock()
otro_datalock = threading.Lock()
# thread handler
yourThread = threading.Thread()
otrohilo = threading.Thread()

def create_app():
    app = Flask(__name__)

    def interrupt():
        global yourThread
        yourThread.cancel()

    def doStuff():
        global commonDataStruct
        global yourThread
        with dataLock:
            yourThread = threading.Timer(POOL_TIME, doStuff, ())
            print("estoy haciendo algo en el back")
            yourThread.start()   

    def haz_otr_cosa():
        global otrohilo
        global ledSts
        global sensLuzSts

        with otro_datalock:
            otrohilo = threading.Timer(10, haz_otr_cosa, ())
            print("otro hilo bro")
            ledSts = ''.join(random.choice(GENES_POSIBLES) for i in range(10))
            print(ledSts)
            sensLuzSts = 150
            otrohilo.start() 

    def doStuffStart():
        # Do initialisation stuff here
        global yourThread
        # Create your thread
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        print("estoy haciendo otra cosa?")
        yourThread.start()


    def hacer_comernzar_otro_hilo():
        global otrohilo
        otrohilo = threading.Timer(10, haz_otr_cosa, ())
        print("empiezo otro hilo bro")
        otrohilo.start()

    @app.route("/")
    def index():
        global ledSts
        global sensLuzSts

        templateData = {
        'led'  : ledSts,
        'sensorLuz'  : sensLuzSts,

        }
        return render_template('index.html', **templateData)


    # Initiate
    doStuffStart()
    hacer_comernzar_otro_hilo()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app

app = create_app()     