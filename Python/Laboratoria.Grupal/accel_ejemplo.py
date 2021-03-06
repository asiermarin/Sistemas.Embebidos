#@Laura Arjona
#@Sistemas Embebidos. 2020


# Programa ejemplo de uso del acelerómetro MMA7660FC

import smbus
import time
import math

# Seleccionar el bus I2C
bus = smbus.SMBus(1)

# Direcicón I2C del dispositivo
MMA7660FC_DEFAULT_ADDRESS           = 0x4C

# MMA7660FC Register Map
MMA7660FC_XOUT                      = 0x00 # Output Value X
MMA7660FC_YOUT                      = 0x01 # Output Value Y
MMA7660FC_ZOUT                      = 0x02 # Output Value Z
MMA7660FC_TILT                      = 0x03 # Tilt Status
MMA7660FC_SRST                      = 0x04 # Sampling Rate Status
MMA7660FC_SPCNT                     = 0x05 # Sleep Count
MMA7660FC_INTSU                     = 0x06 # Interrupt Status
MMA7660FC_MODE                      = 0x07 # Mode Register
MMA7660FC_SR                        = 0x08 # Sample Rate Register
MMA7660FC_PDET                      = 0x09 # Tap/Pulse Detection Register
MMA7660FC_PD                        = 0x0A # Tap/Pulse Debounce Count Register

# MMA7660FC Mode Register
MMA7660FC_MODE_STANDBY              = 0x00 # Standby Mode
MMA7660FC_MODE_TEST                 = 0x04 # Test Mode
MMA7660FC_MODE_ACTIVE               = 0x01 # Active Mode
MMA7660FC_AWE_EN                    = 0x08 # Auto-Wake Enabled
MMA7660FC_AWE_DS                    = 0x00 # Auto-Wake Disabled
MMA7660FC_ASE_EN                    = 0x10 # Auto-Sleep Enabled
MMA7660FC_ASE_DS                    = 0x00 # Auto-Sleep Disabled
MMA7660FC_SCPS_16                   = 0x20 # Prescaler is divide by 16
MMA7660FC_SCPS_1                    = 0x00 # Prescaler is divide by 1
MMA7660FC_IPP_OPEN                  = 0x00 # Interrupt output INT is open-drain
MMA7660FC_IPP_PUSH                  = 0x40 # Interrupt output INT is push-pull
MMA7660FC_IAH_LOW                   = 0x00 # Interrupt output INT is active low
MMA7660FC_IAH_HIGH                  = 0x80 # Interrupt output INT is active high

# MMA7660FC Sample Rate Register
MMA7660FC_AMSR_120                  = 0x00 # 120 Samples/Second Active and Auto-Sleep Mode
MMA7660FC_AMSR_64                   = 0x01 # 64 Samples/Second Active and Auto-Sleep Mode
MMA7660FC_AMSR_32                   = 0x02 # 32 Samples/Second Active and Auto-Sleep Mode
MMA7660FC_AMSR_16                   = 0x03 # 16 Samples/Second Active and Auto-Sleep Mode
MMA7660FC_AMSR_8                    = 0x04 # 8 Samples/Second Active and Auto-Sleep Mode
MMA7660FC_AMSR_4                    = 0x05 # 4 Samples/Second Active and Auto-Sleep Mode
MMA7660FC_AMSR_2                    = 0x06 # 2 Samples/Second Active and Auto-Sleep Mode
MMA7660FC_AMSR_1                    = 0x07 # 1 Samples/Second Active and Auto-Sleep Mode
MMA7660FC_AWSR_32                   = 0x00 # 32 Samples/Second Auto-Wake Mode
MMA7660FC_AWSR_16                   = 0x08 # 16 Samples/Second Auto-Wake Mode
MMA7660FC_AWSR_8                    = 0x10 # 8 Samples/Second Auto-Wake Mode
MMA7660FC_AWSR_1                    = 0x18 # 1 Samples/Second Auto-Wake Mode

class MMA7660FC():
    def __init__(self):
        self.mode_config()
        self.sample_rate_config()
    
    #Función para configurar el sensor antes de proceder a las medidas
    def mode_config(self):
        """Select the mode control register of the accelerometer from the given provided values"""
        MODE_CONTROL = (MMA7660FC_MODE_ACTIVE | MMA7660FC_AWE_DS | MMA7660FC_ASE_DS | MMA7660FC_SCPS_1 | MMA7660FC_IAH_LOW)
        bus.write_byte_data(MMA7660FC_DEFAULT_ADDRESS, MMA7660FC_MODE, MODE_CONTROL)
        
    #Función para configurar el registro de interrupciones
    def interrupt_config(self):
        bus.write_byte_data(MMA7660FC_DEFAULT_ADDRESS, MMA7660FC_INTSU, 0xE7)
    
    #Función para configurar el número de muestras por segundo
    def sample_rate_config(self):
        SAMPLE_RATE = (MMA7660FC_AMSR_2)
        bus.write_byte_data(MMA7660FC_DEFAULT_ADDRESS, MMA7660FC_SR, SAMPLE_RATE)
    

    #Función para leer los valores de x,y,z del sensor
    #Parámetros de la función bus.read_i2c_block_data
        #  direcicón I2C del dispositivo (MMA7660FC_DEFAULT_ADDRESS)
        #  donde se comienza a leer (MMA7660FC_XOUT)
        #  cuantos bytes se quiren leer (3)
    def read_accl(self):
        data = bus.read_i2c_block_data(MMA7660FC_DEFAULT_ADDRESS, MMA7660FC_XOUT, 3)
        
        # Se conveirten los datos a 6 bits, porque la trama leída completa son 8 bits, y los dos primeros
        # bits más significativos son de configuración. Los bits de la aceleracion son los bits 6-0
        xAccl = data[0] & 0x3F
        if xAccl > 31 :
            xAccl -= 64
        
        yAccl = data[1] & 0x3F
        if yAccl > 31 :
            yAccl -= 64
        
        zAccl = data[2] & 0x3F
        if zAccl > 31 :
            zAccl -= 64
        
        return {'x' : xAccl, 'y' : yAccl, 'z' : zAccl}

  #Función para leer los bits correspondientes a la orentación del sensor
    #Parámetros de la función bus.read_i2c_block_data
        #  direcicón I2C del dispositivo (MMA7660FC_DEFAULT_ADDRESS)
        #  donde se comienza a leer (MMA7660FC_TILT) -- que es 0x03
        #  cuantos bytes se quiren leer (1)
    def read_orientation(self):
        """Leer datos desde la posicion 0x03, 1 byte """
        data = bus.read_i2c_block_data(MMA7660FC_DEFAULT_ADDRESS, MMA7660FC_TILT, 1)
        
        PoLa = data[0] & 0x1C
        
        if PoLa == 0x00:
            print("Orientacion desconocida")
            orientation = 0 #Desconocido
        elif PoLa == 0x04:
            print("Orientacion izquierda")
            orientation = 1  #Izquierda: Dispositivo esta en modo paisaje hacia la izquierda
        elif PoLa == 0x08:
            print("Orientacion derecha")
            orientation = 2  #Derecha: Dispositivo esta en modo paisaje hacia la derecha
        elif PoLa == 0x14:
            print("Orientacion abajo")
            orientation = 3 # Abajo: Dispositivo está en posición vertical invertida
        elif PoLa == 0x18:
            print("Orientacion arriba")
            orientation = 4 # Arriba: Dispositivo está en posición vertical normal
        else:
            orientation = 0x00
        return orientation    


 # ---------------------- TO DO ----------------
# Actividad Parte 2 - E
    def read_shake(self):
        data = bus.read_i2c_block_data(MMA7660FC_DEFAULT_ADDRESS,MMA7660FC_TILT,1)

        shake = data[0] & 0x80

        if shake == 0x00:
            print("No shake")
        else:
            print("Shake")

 # ---------------------- TO DO ----------------
# Actividad Parte 2 - G
    def contar_pasos(self, eje_x, eje_y, eje_z):
        mag = math.sqrt((eje_x**2) + (eje_y**2) + (eje_z**2))  
        pasos = 0
        if (mag > 30):
            return True
        else:
            return False

 # ------------INICIALIZACIÓN Y CONFIGURACIÓN DEL SENSOR ----------------
mma7660fc = MMA7660FC()
mma7660fc.mode_config()
time.sleep(0.1)
mma7660fc.sample_rate_config()
time.sleep(0.1)
mma7660fc.interrupt_config()
time.sleep(0.1)
 # -------------------------------

pasos = 0
while True :
    time.sleep(0.1)
    mma7660fc.read_orientation()
    mma7660fc.read_shake()
    accl = mma7660fc.read_accl()
    print("Valores en g:")
    print ("Acceleration in X-Axis : %f"%(accl['x']/21.33) + "g")
    print ("Acceleration in Y-Axis : %f"%(accl['y']/21.33)+ "g")
    print ("Acceleration in Z-Axis : %f"%(accl['z']/21.33)+ "g")
    print (" ************************************* ")
    eje_x = accl['x']
    eje_y = accl['y']
    eje_z = accl['z']
    if (mma7660fc.contar_pasos(eje_x, eje_y, eje_z) == True):
        pasos += 1
    print(f"Pasos: {pasos}")
         
# ---------------------- TO DO ----------------
# Actividad Parte 2 - D
    #imprimir por pantalla los valores de aceleraicón en m/s^2
while True :
    time.sleep(0.1)
    accl = mma7660fc.read_accl()
    print("Valores en m/s2:")
    print ("Acceleration in X-Axis : %f"%((accl['x']/21.33) * 9.8) + " m/s2")
    print ("Acceleration in Y-Axis : %f"%((accl['y']/21.33) * 9.8)+ " m/s2")
    print ("Acceleration in Z-Axis : %f"%((accl['z']/21.33) * 9.8)+ " m/s2")
    print (" ************************************* ")
# ---------------------- ----------------------
 