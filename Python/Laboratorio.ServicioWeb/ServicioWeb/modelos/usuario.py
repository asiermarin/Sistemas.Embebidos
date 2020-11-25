from sqlalchemy import SQLAlchemy

class Usuario(base):

    def __init__(self, nombre, email, contrasenia):
        self.nombre = nombre
        self.email = email
        self.contrasenia = contrasenia

    __tablename__ = 'usuario'