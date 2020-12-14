from comun.singleton import Singleton
from servicios.weblogging import Applogging
from static.constantes import SECUANCIA_SEGUNDOS_RPI
import threading
import atexit

class Rpi(metaclass=Singleton):
# class Rpi:
    
    def __init__(self):
        self.__rpi_log = Applogging("RPI")
        self.__hilo_datalock = threading.Lock()
        self.__hilo_rpi = threading.Thread()
        self.__sensor_temepratura_interna = None
        self.__comenzar_servicio_background()

    def __obtener_datos_rpi(self):
        with self.__hilo_datalock:
            self.__hilo_rpi = threading.Timer(SECUANCIA_SEGUNDOS_RPI, self.__obtener_datos_rpi, ())
            self.__rpi_log.info_log("Funcionando")
            self.__hilo_rpi.start()

    def __comenzar_servicio_background(self):
        self.__hilo_rpi = threading.Timer(SECUANCIA_SEGUNDOS_RPI, self.__obtener_datos_rpi, ())
        self.__rpi_log.info_log("Servicio RPI comenzando en backgound")
        self.__hilo_rpi.start()
