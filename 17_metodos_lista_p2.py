""" 
    En Python existe distintas formas de copiar una Lista:

    -   Mediante Shalow copy, que en realidad es crear una SubLista completa de la Lista original.
    -   Mediante el método copy(), que realiza una copia de la Lista. 
    -   Mediante la técnica slicing (segmentación) extraemos una porción de una Lista sin modificar
        la original y la invertimos.
    -   Mediante el método reverse(), invertimos una lista modificandola.
"""

#            -5         -4       -3      -2        -1
#             0          1        2       3         4
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # String (5)

""""" Copia de una Lista con (shallow copy) """""
copy_list = courses[:] # shallow copy
print(copy_list) # ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB']


""""" Método Copy - lista.copy() """""
copy_list_2 = courses.copy()
print(copy_list_2) # ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB']

""""" Invertir una Lista con (slicing) """""
reverse_list = courses[::-1] # slicing -> No modifica la Lista original
print(reverse_list) # ['MongoDB', 'Ruby', 'Flask', 'Django', 'Python']
print(courses) # ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB']

""""" Método Reverse - lista.reverse() """""
courses.reverse() # Modifica la Lista original
print(courses) # ['MongoDB', 'Ruby', 'Flask', 'Django', 'Python']