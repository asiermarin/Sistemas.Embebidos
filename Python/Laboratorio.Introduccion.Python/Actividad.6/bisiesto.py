string_year = input("Introduce un año: ")
CONSTANT = "fin"

while (string_year != CONSTANT):
    int_year = int(string_year)
    possible_result_1 = int_year / 4
    possible_result_2 = int_year / 400
    impossible_result = int_year / 100

    if ((possible_result_1.is_integer() or possible_result_2.is_integer()) and 
    not impossible_result.is_integer()):
        print(f"{int_year} es bisiesto")
    else:
        print(f"{int_year} no es bisiesto")

    string_year = input("Introduce un año: ")

# NOTA: utilizar los operadores en la misma linea por que si no parece ser
# que no se aplica bien