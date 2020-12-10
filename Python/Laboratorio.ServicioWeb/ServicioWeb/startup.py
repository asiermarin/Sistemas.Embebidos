from flask import _app_ctx_stack, jsonify
from controladores.indexcontroller import Indexcontroller
from controladores.registrocontroller import Registrocontroller
from servicios.rpi import Rpi
from servicios.weblogging import Applogging
from servicios.mysqlDB import MysqlDB
from servicios.autenticacion import Autenticacion
from modelos import usuario
from testunitarios.dbtest import Test

class Startup:

    def __init__(self, app):
        self.__app = app
        self.__log_startup = Applogging("Startup")
        self.servicio_db = None
        self.servicio_autenticacion = None
        self.__inyeccion_dependencias()

    def __inyeccion_dependencias(self):
        self.__log_startup.info_log("Iniciando instacias de la aplicacion")
        self.__add_servicio_db()
        self.__add_servicio_autenticacion()

    def __add_servicio_db(self):
        try: 
            self.__log_startup.info_log("Iniciando servicio mysql...")
            self.servicio_db = MysqlDB(self.__app, _app_ctx_stack)
            self.__log_startup.info_log("Creando tablas")
            usuario.Base.metadata.create_all(bind = self.servicio_db.engine)
            self.servicio_db.sesion.commit()
            self.servicio_db.sesion.close()  
        except:
            self.__log_startup.error_log("Error a la hora de crear tablas")
        
    def __add_servicio_autenticacion(self):
        self.__log_startup.info_log("Iniciando servicio autenticacion...")
        self.servicio_autenticacion = Autenticacion(self.servicio_db.sesion)

        index_controller_log = Applogging("Controlador Index")
        self.__app.add_url_rule('/', endpoint = 'index', view_func = Indexcontroller.as_view(
            'index', autenticacion = self.servicio_autenticacion, index_controller_log = index_controller_log), methods = ["GET", "POST"])

        registro_controller_log = Applogging("Controlador Registro")
        self.__app.add_url_rule('/registro', endpoint = 'registro', view_func = Registrocontroller.as_view(
            'registro', autenticacion = self.servicio_autenticacion, registro_controller_log = registro_controller_log), methods = ["GET", "POST"])

    def __add_servicio_rpi(self):
        print()
        