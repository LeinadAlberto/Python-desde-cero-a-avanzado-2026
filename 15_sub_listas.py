""" 
    -   A partir de las listas en python podemos generar sub listas y para ello se implementara 
        el concepto de corte o slicing.
    -   Slicing: []
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
new_list_2 = courses[2:5]
print(new_list_2) # ['Flask', 'Ruby', 'MongoDB']