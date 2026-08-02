"""
    Los operadores logicos son 3: 
        and
        or
        not
    Al utilizarlos se tiene como resultado un valor Booleano, True o False.
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

result = (
   False 
   or False 
   or number_one == number_two 
   or number_one < 100 
   or number_two > 200
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