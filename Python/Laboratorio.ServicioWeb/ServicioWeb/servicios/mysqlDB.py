from sqlalchemy import create_engine, exists
from sqlalchemy.ext.declarative import declarative_base
from comun.singleton import Singleton
from servicios.weblogging import Applogging
from sqlalchemy.orm import scoped_session, sessionmaker

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
            usuario = "domotoystgsvr@domotoystgsvr"
            contrasenia = "ySyd,r6Y1h:jNw6"
            ip_host = "domotoystgsvr.mysql.database.azure.com"
            puerto = "3306"
            base_de_datos = "serviciowebdatabase"
            BASE_DE_DATOS_REMOTO = f"mysql://{usuario}:{contrasenia}@{ip_host}:{puerto}/{base_de_datos}"
            # DATABASE_DATOS_LOCAL = 'mysql://adminuser:adminuser@127.0.0.1:7000/ServicioWeb'
            self.__mysql_log.info_log(f"Utilizando direccion: {BASE_DE_DATOS_REMOTO}")
            self.engine = create_engine(BASE_DE_DATOS_REMOTO)
            self.engine.connect()
            Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            self.sesion = Session()
        except:
            self.__mysql_log.error_log("No se han podido iniciar las instancias de la conexion")

    def __obtener_parametros_desde_json(self):
        print()

    def __crear_cadena_conexion(self):
        print()