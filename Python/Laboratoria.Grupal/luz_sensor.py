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

# Output data to screen
print ("Espectro completo(IR + Visible) :%d lux" %ch0)
print ("Valor espectro infrarrojo :%d lux" %ch1)
print ("Valor espectro visible:%d lux" %(ch0 - ch1))

