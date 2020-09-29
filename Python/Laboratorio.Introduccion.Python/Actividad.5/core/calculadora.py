class Calculadora():

    SUM_OPTION_CONSTANT = "1"
    REST_OPTION_CONSTANT = "2"
    ELEVATE_OPTION_CONSTANT = "3"
    LEFT_OPTION_CONSTANT = "4"

    def __init__(self):
        self.init_loop()

    def init_loop(self):
        read_string = None
        read_string = self.export_data()

        while(read_string != self.LEFT_OPTION_CONSTANT):
            if (read_string == self.SUM_OPTION_CONSTANT):
                self.sum()
            elif (read_string == self.REST_OPTION_CONSTANT):
                self.rest()
            elif (read_string == self.ELEVATE_OPTION_CONSTANT):
                self.elevate()
            read_string = self.export_data()

    def export_data(self):
        print("1 ---> SUM")
        print("2 ---> REST")
        print("3 ---> ELEVATE")
        print("4 ---> LEFT")
        read_string = input('Enter a option: ')

        return read_string

    def sum(self):
        value_1 = input('Enter value: ')
        value_2 = input('Enter other value: ')
        total = float(value_1) + float(value_2)
        print(total)

    def rest(self):
        value_1 = input('Enter value: ')
        value_2 = input('Enter other value: ')
        if (float(value_1) > float(value_2)):
            total = float(value_1) - float(value_2)
        else:
            total = float(value_2) - float(value_1)
        print(total)

    def elevate(self):
        base = input('Enter base value: ')
        elevate_number = input('Enter elevate value: ')

        total = 0
        count = 0
        while(count < int(elevate_number)):
            count += 1
            total = total * int(base)
        print(total)
