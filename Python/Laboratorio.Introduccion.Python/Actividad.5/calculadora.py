class Calculadora():

    SUM_OPTION_CONSTANT = "1"
    REST_OPTION_CONSTANT = "2"
    ELEVATE_OPTION_CONSTANT = "3"
    LEFT_OPTION_CONSTANT = "4"

    def __init__(self):
        init_bucle()

    def init_bucle(self):
        read_string = None
        export_data()

        while(read_string == LEFT_OPTION_CONSTANT):
            if (read_string == SUM_OPTION_CONSTANT):
                sum()
            elif (read_string == REST_OPTION_CONSTANT):
                rest()
            elif (read_string == REST_OPTION_CONSTANT):
                rest()
            else: 
                read_string = LEFT_OPTION_CONSTANT
            export_data()

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
        total = value_1 + value_2
        print(total)

    def rest(self):
        value_1 = input('Enter value: ')
        value_2 = input('Enter other value: ')
        if (value_1 > value_2):
            total = value_1 - value_2
        else:
            total = value_2 - value_1
        print(total)

    def elevate(self):
        base = input('Enter base value: ')
        elevate_number = input('Enter elevate value: ')

        total = 0
        count = 0
        while(count < elevate_number):
            count += 1
            total *= base
        print(total)
