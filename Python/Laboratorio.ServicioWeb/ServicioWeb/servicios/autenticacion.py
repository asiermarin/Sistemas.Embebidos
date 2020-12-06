from comun.singleton import Singleton
from servicios.weblogging import Applogging

class Autenticacion(metaclass=Singleton):

    def __init__(self, sesion):
        self.__autenticacion_log = Applogging("Autenticacion")
        self.__sesion = sesion
        self.usuario_autenticado = False

    def crear_usuario(self):
        print()

    def comprobar_autenticacion(self, usuario_form, contrasenia_form):
        print()
