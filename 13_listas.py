"""
    -   Una lista es una estructura de datos, una colección que nos permite almacenar
        y gestionar otros tipos de datos, tipos como strings, enteros, flotantes, booleanos
        y otras listas.

    -   Sintaxis
        <variable> = []

    -   Recomendable solo trabajar con listas homogeneas que manejen un solo tipo de dato.

    -   Todas las listas se rigen por la regla de los indices, comenzando por el primer elemento
        con el indice 0 y asi sucesivamente con incremento de 1.
"""

my_list = ["String", 10, 3.14, True, [1, 2, 3]]

print(my_list) # ['String', 10, 3.14, True, [1, 2, 3]]
print(type(my_list)) # <class 'list'>

print()

#            0          1        2        3        4      # Lista de 5 elementos
cursos = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Lista de elementos tipo Strings
print(cursos)

numbers = [1, 2, 3, 4, 5] # Lista de elementos tipo Enteros
print(numbers)