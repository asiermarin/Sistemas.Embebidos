#@Laura Arjona
#@Sistemas Embebidos. 2020

# Programa ejemplo de uso del sensor digital de temperatura y humedad DHT11

import time
import dht_config
import RPi.GPIO as GPIO

GPIO.setmpde(GPIO.BMC)

#Definir una variable para comprobar si el switch está en alto o bajo
Variable_TH = 0 
 
def main():
    #Configurar los pines del sensor de temperatura y del switch con la funcion setup
    # ---- TO DO -----
    GPIO_switch = 24
    GPIO_sensor = 18
    GPIO.setup(GPIO_switch, GPIO.IN)

    #Crear una instancia del sensor de temperatura. Mirad el fichero dht_config.py para detalles de configuración
    sensor = dht_config.DHT(GPIO_sensor) #Pasar por argumento el número del GPIO
 
    #Función que vamos a llamar con el callback
    def procesar(numcanal):
        #para poder usar la variable dentro del thread del callback, hay que declararla como global
        global Variable_TH 
        
        if GPIO.input(GPIO_switch):
            # ---- TO DO -----
            Variable_TH = 1
        else:
            # ---- TO DO -----
            Variable_TH = 0        
            print("SWITCH OFF")  
    
    #Añadir un evento de call back al GPIO del switch, que se llame procesar()
    # # ---- TO DO -----
    GPIO.setup(GPIO_switch, GPIO.IN)
    GPIO.add_event_detect(GPIO_switch, GPIO.BOTH, callback=procesar)
        
    while True:
        #If-ese:  si el swtich está HIGH, mostrar por pantalla los valores de temperatura, cada 1 segundo
        #si el switch está LOW, parar la lectura del sensor
        # -- TO DO ---
        if Variable_TH == 1:
            humedad, temp = sensor.read()
            print('Temperatura {0:.1f}'.format(temp))
            time.sleep(1)

if __name__ == '__main__':
    main()