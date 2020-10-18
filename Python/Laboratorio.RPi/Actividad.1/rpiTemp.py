#!/usr/bin/env python3
import subprocess
import os
import time

def medir_temperatura():
    cpu = subprocess.check_output('sudo cat /sys/class/thermal/thermal_zone0/temp', shell=True)
    cpu_c = int(cpu)/1000       # Se divide en en 1000 por que muestra decimales, ej; 48320
    print(cpu_c)  
    return cpu_c

def parpadear_led():
    os.system('modprobe ledtrig_heartbeat')
    resultado = os.system('echo heartbeat >/sys/class/leds/led0/trigger')
    return resultado

def dejar_parpadear(): 
    os.system('echo 0 >/sys/class/leds/led0/brightness')
    print("HA DEJADO DE PARPADEAR")

if __name__ == '__main__':
    TIEMPO_ESPERA_HASTA_COMRPROBAR = 5.0 # 2 seg
    empezar_temporizar = time.time()
    diferencia_tiempo = 0.0
    resultado = None
    while((medir_temperatura() > 40)):
        tiempo_hasta_ahora = time.time()
        diferencia_tiempo = tiempo_hasta_ahora - empezar_temporizar
        if((TIEMPO_ESPERA_HASTA_COMRPROBAR <= diferencia_tiempo) and resultado != 0): # Se utiliza resultado para 
                                                                                      # comprobar que ya se ha encendido
            print(f"segundos: {diferencia_tiempo}")
            resultado = parpadear_led()
            if(resultado == 0):
                print("LED PARPADEANDO")
            TIEMPO_ESPERA_HASTA_COMRPROBAR = TIEMPO_ESPERA_HASTA_COMRPROBAR + 5.0
    dejar_parpadear()