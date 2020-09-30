from models.sensor import Sensor
from models.medida import Medida

class Startup:

    CREAR_MEDIDA_CONSTANTE = "1"
    SALIR_CONSTANTE = "2"

    _sensor = sensor

    def __init__(self):
        iniciar_bucle()

    def iniciar_bucle(self):
        print("----- BIENVENIDO ------------")
        string_estrada = None
        string_entrada = self.mostrar_en_pantalla()

        while(string_estrada != self.CREAR_MEDIDA_CONSTANTE):
            if (string_estrada == self.SUM_OPTION_CONSTANT):
               
            read_string = self.export_data()

    def mostrar_en_pantalla(self):
        print("1 ---> CREAR MEDIDA")
        print("2 ---> SALIR")
        read_string = input('Introduce la opcion: ')