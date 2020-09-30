class Sensor:

    def __init__(self, tipo, lista_medidas):
        self.tipo = tipo
        self.lista_medidas = lista_medidas

    def mostrar_sensor(self):
        print("------------------------------------")
        print(f"{self.tipo} con medidas:")
        for i in range(len(self.lista_medidas)):
            self.lista_medidas[i].mostrar_medida()
        print("------------------------------------")
            