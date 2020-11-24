
# --------------------------------------------------------------
#     EJEMPLO DE SERVICIO WEB CON FLASK - INTEGRA HTML Y CSS 
# --------------------------------------------------------------
#@Laura Arjona
#@Sistemas Embebidos. 2020
# -----------------------------------

import RPi.GPIO as GPIO
from flask import Flask, render_template, request


import smbus
import time

# Acceso al bus I2C para conectarnos al senso de luz
bus = smbus.SMBus(1)
#Dirección I2C del sensor de Luz
TSL2561_DEFAULT_ADDRESS   = 0x29
bus.write_byte_data(TSL2561_DEFAULT_ADDRESS, 0x00 | 0x80, 0x03)
bus.write_byte_data(TSL2561_DEFAULT_ADDRESS, 0x01 | 0x80, 0x02)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO pin para el LED
led = 17
GPIO.setup(led, GPIO.OUT)   

#Inicializar las variables que vamos a asociar al HTML
ledSts = 0
sensLuzSts = 0

# Valor inicial del led
# turn led OFF 
GPIO.output(led, GPIO.LOW)


#instancia de la app de Flask
app = Flask(__name__)


#Función del directorio raiz
@app.route("/")
def index():
    # Read GPIO Status
    ledSts = GPIO.input(led)
    sensLuzSts = 150
    templateData = {
      'led'  : ledSts,
      'sensorLuz'  : sensLuzSts,

      }
    return render_template('index.html', **templateData)


#Función cuando se hace click en el boton de encender o apagar led
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'led':
        actuator = led  
    if action == "on":
        GPIO.output(actuator, GPIO.LOW) #Encender el LED
        ledSts =1
    if action == "off":
        GPIO.output(actuator, GPIO.HIGH) #Apagar el LED
        ledSts =0       
 
    ledSts = GPIO.input(led)

   #Asociamos las variables al HTML (index.html)
    templateData = {
      'led'  : ledSts,
      'sensorLuz'  : sensLuzSts,
    }
    return render_template('index.html', **templateData)



#Función cuando se hace click en el boton de Leer valor del sensor de luz
@app.route("/<sensor>")
def read_sensor(sensor):
    
    sensLuzSts = 0
    if sensor == 'sensorluz':
        sensLuzSts = read_luz()

    ledSts = GPIO.input(led) #variable de estado del LED: lectura del pin
  
    templateData = {
      'sensorLuz'  : sensLuzSts,
      'led'  : ledSts,
    }
    #Asociamos las variables al HTML (index.html)
    return render_template('index.html', **templateData)


# Función para leer el valor de lumninosidad en LUX del espectro visible
def read_luz():
    data = bus.read_i2c_block_data(TSL2561_DEFAULT_ADDRESS, 0x0C | 0x80, 2)
    data1 = bus.read_i2c_block_data(TSL2561_DEFAULT_ADDRESS, 0x0E | 0x80, 2)
    ch0 = data[1] * 256 + data[0] #shift dataHigh to uppber byte
    ch1 = data1[1] * 256 + data1[0] #shift dataHigh to upper byte
    return ch0 - ch1


#Es necesario incluir el host 0.0.0.0 para poder acceder al servicio
#desde fuera de la RPi donde estamos ejecutando este servicio
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
