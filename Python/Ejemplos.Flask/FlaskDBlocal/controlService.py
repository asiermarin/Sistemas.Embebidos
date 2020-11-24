# --------------------------------------------------------------
#     Ejemplo monitorización sensores
#     Laboratorio 7
# --------------------------------------------------------------
#   @Laura Arjona
#  @Sistemas Embebidos. 2020
# -----------------------------------


import RPi.GPIO as GPIO
import sqlite3
import time
from time import sleep
from random import randint
from datetime import datetime

DATABASE = 'db/database.db'


def insert_medida_presion(measurementid,value,date):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO 'measurement-values' (measurementid, value,datetime) VALUES (?,?,?)", (measurementid, value,date))
    conn.commit()
    conn.close()
  
    
def read_presion():  
    valor = randint(0, 101325) #emulación de lectura del sensor de presion en pascales
    return valor
    

if __name__ == "__main__":
   
  
   while 1:
       sleep(2)
       
       valor_presion = read_presion()
       print(valor_presion)
       now = datetime.now()
       fecha  = now.strftime("%d/%m/%Y %H:%M:%S")
       measurementid = 6 #corresponde a presion en pascales
       
       insert_medida_presion(measurementid,valor_presion,fecha)


