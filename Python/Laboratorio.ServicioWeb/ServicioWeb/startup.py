from controltemp import Controltemp
from sensortemp import Sensortemperatura
from weblogging import Applogging

class Startup:

    def __init__(self, app):
        self.__app = app
        self.__log = Applogging("Startup")
        self.__controlador_temperatura = None
        self.__servicio_sensor_temp = None
        self.__inyeccion_dependencias()

    def __inyeccion_dependencias(self):
        self.__log.info_log("Inicio de la aplicacion")

    