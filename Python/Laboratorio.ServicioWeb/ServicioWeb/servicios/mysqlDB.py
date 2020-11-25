from comun.singleton import Singleton

class MysqlDB(metaclass=Singleton):
    
    def __init__(self, app):
        self.__app = app
        self.estado_conexion = False
        self.__init_configuracion(app)

    def __init_configuracion(self, app):
