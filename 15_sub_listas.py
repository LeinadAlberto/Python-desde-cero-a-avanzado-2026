""" 
    -   A partir de las listas en python podemos generar sub listas y para ello se implementara 
        el concepto de corte o slicing.
    -   Slicing: [start:end:skips]
"""
#             0          1        2        3        4
#            -5         -4       -3       -2       -1
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Strings [5]

# new_list = [courses[0], courses[1], courses[3]] 
# print(new_list) # ['Python', 'Django', 'Ruby']

# Obtener los primeros 3 elementos de la lista
# new_list = courses[0:3]
new_list = courses[:3] # Esto es equivalente a escribir --> new_list = courses[0:3]
print(new_list) # ['Python', 'Django', 'Flask']

# Obtener los 3 ultimos elementos de la lista
# new_list_2 = courses[2:5]
new_list_2 = courses[2:] # Esto es equivalente a escribir --> new_list_2 = courses[2:5]
print(new_list_2) # ['Flask', 'Ruby', 'MongoDB']

# Con todo esto podemos tambien obtener una copia de la lista (Shallow copy)
courses_copy = courses[:] # Crea una copia desde el indice 0 hasta el ultimo elemento de la Lista.
print(courses_copy) # ["Python", "Django", "Flask", "Ruby", "MongoDB"]

# Crear una copia desde el primer elemento, hasta el ultimo con saldo de 2. (star:end:2)
courses_copy_2 = courses[::2]
print(courses_copy_2)

# Con slicing tambien podemos invertir los elementos de una lista
lista_invertida = courses[::-1] 
print(lista_invertida) # ['MongoDB', 'Ruby', 'Flask', 'Django', 'Python']