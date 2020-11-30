from comun.singleton import Singleton

class Autenticacion(metaclass=Singleton):

    def __init__(self):
        self.__autenticacion_log = Applogging("Autenticacion")