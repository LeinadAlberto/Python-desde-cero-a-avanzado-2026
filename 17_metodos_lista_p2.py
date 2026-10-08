""" 
    En Python existe distintas formas de copiar una Lista:

    -   Mediante Shalow copy, que en realidad es crear una SubLista completa de la Lista original.
    -   Mediante el método copy(), que realiza una copia de la Lista. 
"""

#            -5         -4       -3      -2        -1
#             0          1        2       3         4
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # String (5)

""""" Copia de una Lista con Shalow copy """""
copy_list = courses[:] # Shalow copy
print(copy_list) # ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB']


""""" Método Copy - lista.copy() """""
copy_list_2 = courses.copy()
print(copy_list_2) # ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB']