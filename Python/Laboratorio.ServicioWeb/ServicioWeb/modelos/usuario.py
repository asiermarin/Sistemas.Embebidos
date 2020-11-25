from sqlalchemy import SQLAlchemy
from run import db

class Usuario():

    def __init__(self, nombre, email, contrasenia):
        self.nombre = nombre
        self.email = email
        self.contrasenia = contrasenia

    __tablename__ = 'usuario'