#@Laura Arjona
#@Sistemas Embebidos. 2020


# Programa ejemplo de uso del Sensor digital de luz TSL2561

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

TSL2561_DEFAULT_ADDRESS           = 0x29


# Seleccionar el registro de control, 0x00(00) con el registro de comandos 0x80
#       Escribir el valor 0x03(03) que corresponde con   Power ON mode
bus.write_byte_data(TSL2561_DEFAULT_ADDRESS, 0x00 | 0x80, 0x03)

# Seleccionar el  timing register 0x01(01) con el registro de comandos 0x80
#       Escribir el valor 0x02(02)    
x = bus.write_byte_data(TSL2561_DEFAULT_ADDRESS, 0x01 | 0x80, 0x01)
print(x)

time.sleep(0.5)

# Leer 2 bytes de data del registro 0x0C 
# ch0 LSB, ch0 MSB
data = bus.read_i2c_block_data(TSL2561_DEFAULT_ADDRESS, 0x0C | 0x80, 2)

# Leer 2 bytes de data del registro 0x0E
# ch1 LSB, ch1 MSB
data1 = bus.read_i2c_block_data(TSL2561_DEFAULT_ADDRESS, 0x0E | 0x80, 2)

# Convertir los valores a enteros
ch0 = data[1] * 256 + data[0] #shift dataHigh to uppber byte
ch1 = data1[1] * 256 + data1[0] #shift dataHigh to upper byte

if (ch0 < 10):
    print("Negro total")
elif (ch0 >= 11 and ch0 <= 50):
    print(" Muy negro")
elif (ch0 >= 51 and ch0 <= 200):
    print("Oscuro en el interior")
elif (ch0 >= 201 and ch0 <= 400):
    print("Tenue en el interior")
elif (ch0 >= 401 and ch0 <= 1000):
    print("Normal")
elif (ch0 >= 1001 and ch0 <= 5000):
    print("Luminsoso")
elif (ch0 >= 5001 and ch0 <= 10000):
    print("Luminoso en el exterior")
elif (ch0 >= 10001 and ch0 <= 30000):
    print("Muy luminoso en el exterior")
elif (ch0 >= 30001 and ch0 <= 100000):
    print("Luz directa")

# Output data to screen
print ("Espectro completo(IR + Visible) :%d lux" %ch0)
print ("Valor espectro infrarrojo :%d lux" %ch1)
print ("Valor espectro visible:%d lux" %(ch0 - ch1))

