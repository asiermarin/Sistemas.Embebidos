from sqlalchemy import SQLAlchemy
from controladores.controladortemp import Controladortemp
from servicios.sensortemp import Sensortemperatura
from servicios.weblogging import Applogging
from servicios.mysqlDB import MysqlDB

class Startup:

    def __init__(self, app):
        self.__app = app
        self.__log_startup = Applogging("Startup")
        self.__servicio_db = None
        self.__inyeccion_dependencias()

    def __inyeccion_dependencias(self):
        self.__log_startup.info_log("Inicioando instacias de la aplicacion")
        self.__add_servicio_db()

    def __add_servicio_db(self):
        self.__log_startup.info_log("Iniciando servicio mysql...")
        log_servicio_db = Applogging("Mysql")
        self.__app.config['MYSQL_HOST'] = '127.0.0.1'
        self.__app.config['MYSQL_USER'] = 'adminuser'
        self.__app.config['MYSQL_PASSWORD'] = 'adminuser'
        self.__app.config['MYSQL_DB'] = 'ServicioWeb'
        db = SQLAlchemy(self.__app)
        self.__servicio_db = MysqlDB(self.__app, log_servicio_db)


    def __add_servicio_autenticacion(self):
        self.__log_startup.info_log("Iniciando servicio autenticacion...")