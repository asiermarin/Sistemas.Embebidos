from modelos.usuario import Usuario
from comun.singleton import Singleton

class Test(metaclass=Singleton):

    def conexion_is_ok(self, sesion):
            usuario_random = Usuario("Asier", "asier@usto.es", "xxxxxx")
            sesion.add(usuario_random)
            sesion.commit()
            sesion.close()
