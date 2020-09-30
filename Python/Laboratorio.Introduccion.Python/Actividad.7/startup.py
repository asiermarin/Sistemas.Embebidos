from models.sensor import Sensor
from models.medida import Medida

class Startup:
    
    PATH_FICHERO = "./sensor.txt"
    CREAR_MEDIDA_CONSTANTE = '1'
    SALIR_CONSTANTE = '2'
    _sensor = None

    def __init__(self):
        lista_medidas = []
        tipo = "Sensor de temperatura"
        self._sensor = Sensor(tipo, lista_medidas)
        self.iniciar_bucle()

    def iniciar_bucle(self):
        fichero = self.__crear_en_fichero()
        print("----- BIENVENIDO ------------")
        string_entrada = None

        while(string_entrada != self.SALIR_CONSTANTE):
            string_entrada = self.mostrar_en_pantalla()
            if (string_entrada == self.CREAR_MEDIDA_CONSTANTE):
                fichero = self.__abrir_fichero(fichero)
                valor = input('Introduce el valor de la medida: ')
                unidad = input('Introduce el tipo de unidad: ')
                medida = Medida(valor, unidad)
                self._sensor.lista_medidas.append(medida)
                fichero = self.__escribir_y_cerrar(fichero)
            self._sensor.mostrar_sensor()

    def mostrar_en_pantalla(self):
        print("1 ---> CREAR MEDIDA")
        print("2 ---> SALIR")
        string_entrada = input('Introduce la opcion: ')
        return string_entrada

    def __crear_en_fichero(self):
        fichero = open(self.PATH_FICHERO,"w+")
        return fichero

    def __abrir_fichero(self, fichero):
        fichero = open(self.PATH_FICHERO,"a+")
        return fichero

    def __escribir_y_cerrar(self, fichero):
        fichero.write(str(self._sensor.tipo) + ":")
        for i in range(len(self._sensor.lista_medidas)):
            fichero.write(str(self._sensor.lista_medidas[i].str_medida()+ "%d\r\n" % (i+1)))
        fichero.close()
        return fichero

    