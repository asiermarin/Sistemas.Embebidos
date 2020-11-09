# -----------------------------------
#     MQTT CLIENT DEMO 
# -----------------------------------
#@Laura Arjona
#@Sistemas Embebidos. 2020
# -----------------------------------

 
import paho.mqtt.client as mqtt
import json


topic = "deustoLab/aceleracion"


# Callback que se llama cuando el cliente recibe el CONNACK del servidor 
#Restult code 0 significa conexion sin errores
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Nos subscribirmos al topic 
    client.subscribe(topic)
 #-----------------------------------------------
# Callback que se llama "automaticamente" cuando se recibe un mensaje del Publiser.
def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    mensaje_recibido = msg.payload
    print(msg.topic+" "+mensaje_recibido)

    #the message received starts with 'b, that mean bytes. 
    mensaje_recibido_json =json.loads(msg.payload )
   
    varx=mensaje_recibido_json["varx"]
    print(varx)

    vary=mensaje_recibido_json["vary"]
    print(vary)

    varz=mensaje_recibido_json["varz"]
    print(varz)
 #-----------------------------------------------
 # Creamos un cliente MQTT 
client = mqtt.Client()

#Definimos los callbacks para conectarnos y subscribirnos al topic
client.on_connect = on_connect
client.on_message = on_message

#Para la actividad 1: usad la IP de la RPi que actúa como broker
#hostname =""

#Para la actividad 2: usad la IP del servidor gratutio de mosquitto
hostname = "test.mosquitto.org"
 
client.connect(hostname, 1883, 60)
client.loop_forever()