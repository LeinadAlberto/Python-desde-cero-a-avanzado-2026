"""
    Operadores lógicos en Python.

    Python dispone de tres operadores lógicos:

    - and:  Devuelve True únicamente si todas las expresiones evaluadas son True.
            Si al menos una expresión es False, el resultado será False.

    - or:   Devuelve True si al menos una de las expresiones evaluadas es True.
            Solo devuelve False cuando todas las expresiones son False.

    - not:  Niega (invierte) un valor booleano.
            True  -> False
            False -> True

    Los operadores lógicos siempre producen un valor booleano (True o False) cuando
    se utilizan para evaluar expresiones lógicas.
"""

number_one = 10
number_two = 20

# result = True and True # True

# result = True and True and number_one == number_two # False

# result = True and True and number_one != number_two # True

# result = True and True and number_one != number_two and number_one < 100 and number_two > 200 # False

# result = (
#    True 
#    and True 
#    and number_one != number_two 
#    and number_one < 100 
#    and number_two > 200
# ) # False

# result = (
#    True 
#    or True 
#    or number_one != number_two 
#    or number_one < 100 
#    or number_two > 200
# ) # True

# result = (
#    False 
#    or False 
#    or number_one == number_two 
#    or number_one < 100 
#    or number_two > 200
# ) # True

# result = (
#    False 
#    or False 
#    or number_one == number_two 
#    or number_one < 100 
#    or number_two > 200
# ) # True

result = not (
   (number_one == number_two and True) 
   and (number_one < 100)  
   and (number_two < 100)  
   or (number_one > 100 and number_two > 200) 
) # True

print()
print(result) # True
print(type(result)) # <class 'bool'>

# Negación del resultado
print()
print(not result) # False

print()
print(not not result) # True

print()
print(not not not result) # False