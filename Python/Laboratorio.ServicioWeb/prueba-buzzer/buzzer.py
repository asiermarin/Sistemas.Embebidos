import subprocess
import os
import time
import threading
import atexit
try:
    import RPi.GPIO as GPIO
except:
    print("No se puede importar")

hilo_datalock = threading.Lock()
hilo = threading.Thread()
pin = 17
pitando = False

def comenzar_servicio():
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)
    except:
        print("No se puede comenzar el servicio")
    hilo = threading.Timer(0, utilizar_buzzer, ())
    print("Comenzando...")
    hilo.start()

def utilizar_buzzer():
    try:
        hilo = threading.Timer(3, utilizar_buzzer, ())
        global pitando
        print(f"Pitando: {pitando}")
        if (pitando == False):
            GPIO.output(pin, GPIO.HIGH)
            pitando = True
        else:
            GPIO.output(pin, GPIO.OUT)
            pitando = False
    except:
        print("error al utilizar buzzer")
    with hilo_datalock:
        hilo.start()

if __name__ == '__main__':
    comenzar_servicio()
