from modelos.usuario import Usuario
from comun.singleton import Singleton

class Test(metaclass=Singleton):

    def probar_insert_select(self, sesion):
        usuario_random = Usuario("Asier", "asier@usto.es", "unacontrasenia")
        self.sesion.add(usuario_random)
        self.sesion.commit()
        self.sesion.close()
        usuario_anteriormente_creado = self.sesion.query(Usuario).filter_by(nombre = "Asier").first()
        x = usuario_anteriormente_creado.get_contrasenia()
        print(x)
