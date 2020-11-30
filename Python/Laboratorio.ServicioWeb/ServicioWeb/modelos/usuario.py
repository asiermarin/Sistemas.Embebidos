from sqlalchemy import Column, Integer, String
from servicios.mysqlDB import Base
from sqlalchemy_utils import EmailType, PasswordType
from fernet import Fernet

class Usuario(Base):
    
    def __init__(self, nombre, email, contrasenia):
        self.nombre = nombre
        self.email = email
        self.__clave = Fernet.generate_key()
        self.__token = self.__encrypt(contrasenia.encode(), self.__clave)

    def get_contrasenia(self):
        contrasenia_desencriptada = self.__decrypt(self.__token, self.__clave).decode()
        return contrasenia_desencriptada

    def __encrypt(self, message: bytes, key: bytes) -> bytes:
        return Fernet(key).encrypt(message)

    def __decrypt(self, token: bytes, key: bytes) -> bytes:
        return Fernet(key).decrypt(token)

    
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key = True, index = True, nullable = False)
    nombre = Column(String(15), index = True, nullable = False)
    # email = Column(String(25), index = True, unique = True)
    email = Column(EmailType)
    __clave = Column(String(70), index = True, nullable = False)
    __token = Column(String(200), index = True, nullable = False)

