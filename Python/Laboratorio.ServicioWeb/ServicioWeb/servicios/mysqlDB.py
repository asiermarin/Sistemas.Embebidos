from sqlalchemy import create_engine, exists
from sqlalchemy.ext.declarative import declarative_base
from comun.singleton import Singleton
from servicios.weblogging import Applogging
from sqlalchemy.orm import scoped_session, sessionmaker
import json

Base = declarative_base()

class MysqlDB(metaclass=Singleton):

    def __init__(self, app, _app_ctx_stack):
        self.__app = app
        self.__mysql_log = Applogging("MysqlDB")
        self.engine = None
        self.sesion = None
        self.__init_configuracion(_app_ctx_stack)
        
    def __init_configuracion(self, _app_ctx_stack):
        try:
            BASE_DE_DATOS_REMOTO = self.__obtener_parametros_servidor_desde_json()
            # DATABASE_DOCKER_LOCAL = 'mysql://adminuser:adminuser@127.0.0.1:7000/ServicioWeb'
            self.__mysql_log.info_log(f"Utilizando direccion: {BASE_DE_DATOS_REMOTO}")
            self.engine = create_engine(BASE_DE_DATOS_REMOTO)
            self.engine.connect()
            Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            self.sesion = Session()
        except:
            self.__mysql_log.error_log("No se han podido iniciar las instancias de la conexion")

    def __obtener_parametros_servidor_desde_json(self):
        try:
            cadena_conexion = None
            with open("serversettings.json") as server_settings_json:
                datos = json.load(server_settings_json)
                self.__mysql_log.info_log(datos)
                for configuracion in datos['settings']:
                    usuario = configuracion['admin-user']
                    contrasenia = configuracion['password']
                    ip_host = configuracion['host']
                    puerto = configuracion['port']
                    base_de_datos = configuracion['db']
                    cadena_conexion = self.__crear_cadena_conexion(usuario, contrasenia, ip_host, puerto, base_de_datos)
            return cadena_conexion
        except:
            self.__mysql_log.error_log("No se ha podido obtener las credenciales de servidor remoto")

    def __crear_cadena_conexion(self, usuario, contrasenia, ip_host, puerto, base_de_datos):
        return f"mysql://{usuario}:{contrasenia}@{ip_host}:{puerto}/{base_de_datos}"