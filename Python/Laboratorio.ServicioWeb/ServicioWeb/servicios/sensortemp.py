class Sensortemperatura:

    def crear_instancia_si_no_existe(self):
        if (self.sensortemperatura == None):
            self.__sensortemepratura = Sensortemperatura()
        return self.__sensortemepratura
    
    def __init__(self):
        self.__sensortemepratura
