#@Laura Arjona
#@Sistemas Embebidos. 2020

import time
import dht_config
import RPi.GPIO as GPIO

medicion = 0 

GPIO.setmode(GPIO.BCM)


global gpio_pin_switch


callback=True

gpio_pin_switch=24  
gpio_pin_sensorTH = 18
GPIO.setup(gpio_pin_switch, GPIO.IN)

    
sensor = dht_config.DHT(gpio_pin_sensorTH)

def medir():
    humi, temp = sensor.read()
    print('Temperatura {0:.1f}'.format(temp))
    medicion = 0
   
def gestionSwitch(numcanal):
    
    global medicion
    
    medicion = GPIO.input(24)
    
    if medicion:
        print("SWITCH OFF")

if callback:
    GPIO.setup(gpio_pin_switch, GPIO.IN)
    GPIO.add_event_detect(24, GPIO.BOTH, callback=gestionSwitch)            
   
def main():
    while True:
        time.sleep(1)
        
        if medicion:
            medir()
            

if __name__ == '__main__':
    main()
