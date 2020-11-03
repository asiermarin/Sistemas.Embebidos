#@Laura Arjona
#@Sistemas Embebidos. 2020


# Programa ejemplo de uso del sensor digital de temperatura y humedad DHT11

import time
import dht_config
import RPi.GPIO as GPIO

#Definir una variable para comprobar si el switch está en alto o bajo
myVariableCompartida = 0 
 
def main():
    
    #Configurar los pines del sensor de temperatura y del switch con la funcion setup
    # ---- TO DO -----
    gpio_pin_switch = 
    gpio_pin_sensorTH = 


    
    #Crear una instancia del sensor de temperatura. Mirad el fichero dht_config.py para detalles de configuración
    sensor = dht_config.DHT(gpio_pin_sensor) #Pasar por argumento el número del GPIO
    

 
    #Función que vamos a llamar con el callback
    def procesar(numcanal):
        #para poder usar la variable dentro del thread del callback, hay que declararla como global
        global myVariableCompartida
        
        if GPIO.input(gpio_pin_switch):
            # ---- TO DO -----

            print("Lectura activa")
        else:
            # ---- TO DO -----

            print("Stop lectura")

    
    
    #Añadir un evento de call back al GPIO del switch, que se llame procesar()
    # # ---- TO DO -----


        
    while True:
        #If-ese:  si el swtich está HIGH, mostrar por pantalla los valores de temperatura, cada 1 segundo
        #si el switch está LOW, parar la lectura del sensor
        # -- TO DO ---
   


if __name__ == '__main__':
    main()