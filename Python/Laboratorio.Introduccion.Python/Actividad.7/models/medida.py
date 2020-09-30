class Medida:

    def __init__(self, valor, unidad):
        self.valor = valor
        self.unidad = unidad

    def mostrar_medida(self):
        return print(f"{self.unidad} ===> {self.valor}")

    def str_medida(self):
        string_valor = "    Medida en " + str(self.unidad) + " con valor " + str(self.valor)
        return string_valor

