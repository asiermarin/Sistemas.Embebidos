from controltemp import Controltemp
from sensortemp import Sensortemperatura
from servicios.weblogging import Applogging

class Startup:

    def __init__(self, app):
        self.__app = app
        self.__log = Applogging("Startup")
        self.__servicio_db = None
        self.__inyeccion_dependencias()

    def __inyeccion_dependencias(self):
        self.__log.info_log("Inicioando instacias de la aplicacion")

    def __add_servicio_db(self):

    