"""
    Los operadores relacionales son los siguientes:
    ==      Igual que
    >       Mayor que
    >=      Mayor igual que
    <       Menor que
    <=      Menor igual que
    !=      Distinto de

    Nos permiten comparar números enteros o flotantes.
    El resultado de dicha comparación sera un valor Booleano, True o False.
"""

number_one = 10.84
number_two = 10.83

# result = number_one == number_two
# result = number_one > number_two
# result = number_one >= number_two
# result = number_one < number_two
# result = number_one <= number_two
result = number_one != number_two

print()
print(result) # True
print(type(result)) # <class 'bool'>