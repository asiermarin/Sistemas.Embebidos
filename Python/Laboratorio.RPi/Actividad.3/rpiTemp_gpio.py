#!/usr/bin/env python3
# Esta vez he creado una clase para que este mas organizado

import subprocess
import os
import time
from threading import Event # la funcion sleep() no funciona dentro del blucle, se utiliza este

class RpiTemp():

    def __init__(self):
        resultado = None
        event = Event()
        while((self.medir_temperatura() > 40)):
            if(resultado != 0):
                resultado = self.parpadear_led_gpio()
                print("LED PARPADEANDO")
            event.wait(5)
        self.dejar_parpadear()

    def medir_temperatura(self):
        cpu = subprocess.check_output('sudo cat /sys/class/thermal/thermal_zone0/temp', shell=True)
        cpu_c = int(cpu)/1000       # Se divide en en 1000 por que muestra decimales, ej; 48320
        print(cpu_c)  
        return cpu_c

    def parpadear_led_gpio(self):
        os.system("echo 18 >/sys/class/gpio/export")
        os.system("echo out >/sys/class/gpio/gpio18/direction")
        resultado = os.system('echo 1 >/sys/class/gpio/gpio18/value')
        return resultado

    def dejar_parpadear(self): 
        os.system('echo 0 >/sys/class/gpio/gpio18/value')
        os.system("echo 17 >/sys/class/gpio/unexport")
        print("HA DEJADO DE PARPADEAR")

if __name__ == '__main__':
    x = RpiTemp()