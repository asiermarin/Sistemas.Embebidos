from flask import _app_ctx_stack, jsonify
from flask_cors import CORS
from controladores.indexcontroller import Indexcontroller
from servicios.sensortemp import Sensortemperatura
from servicios.weblogging import Applogging
from servicios.mysqlDB import MysqlDB
from servicios.autenticacion import Autenticacion
from modelos import usuario
from testunitarios.dbtest import Test

class Startup:

    def __init__(self, app):
        self.__app = app
        # CORS(self.__app)
        self.__log_startup = Applogging("Startup")
        self.sesion = None
        self.__servicio_db = None
        self.__inyeccion_dependencias()

    def __inyeccion_dependencias(self):
        self.__log_startup.info_log("Iniciando instacias de la aplicacion")
        self.__add_servicio_db()
        self.__add_servicio_autenticacion()

    def __add_servicio_db(self):
        self.__servicio_db = MysqlDB(self.__app, _app_ctx_stack)
        try: 
            self.__log_startup.info_log("Iniciando servicio mysql...")
            self.__servicio_db = MysqlDB(self.__app, _app_ctx_stack)
            self.sesion = self.__servicio_db.sesion
            self.__log_startup.info_log("Creando tablas")
            usuario.Base.metadata.create_all(bind = self.__servicio_db.engine)
            self.sesion.commit()
            self.sesion.close()  
        except:
            self.__log_startup.error_log("Error a la hora de crear tablas")
        
    def __add_servicio_autenticacion(self):
        self.__log_startup.info_log("Iniciando servicio autenticacion...")
        servicio_auth = Autenticacion(self.sesion)
        self.__app.add_url_rule('/index', endpoint = 'index', view_func = Indexcontroller.as_view(
            'index', autenticacion = servicio_auth), methods = ["GET", "POST"])