"""
    Los indices te permiten acceder a los elementos de la colección.
"""
#              0         1        2        3        4
#             -5        -4       -3       -2       -1
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Strings (5)

# Imprimir en consola el primer elemento de la lista.
# value = courses[0]
# print(value) # Python

# Cuando se pide un elemento fuera de rango
# print(courses[5]) # Indice de Lista fuera de rango.


# Obtener el ultimo elemento de la lista cuando desconocemos el indice del ultimo elemento.
# Primero se obtiene cuantos elementos tiene nuestra lista con la función len().

print(
    len(courses) # 5 --> Cantidad de elementos de la lista.
)

# Obteniendo el valor del ultimo indice. 
last_index = len(courses) - 1

print("El ultimo indice vale: ", last_index)

# Con todo eso obtenemos el ultimo elemento de la lista. 
value = courses[last_index]
print("El ultimo elemento de la lista es: ", value) # MongoDB

# En una sola linea de código seria
last_value = courses[len(courses) - 1]
print("El ultimo elemento de la lista es: ", last_value) # MongoDB

# Existe una forma mucho mas paytonica para obtener el ultimo elemento de la lista.
# Usando los indices negativos.

last_value_2 = courses[-1]
print("El ultimo elemento de la lista es: ", last_value_2) # MongoDB

# Modificando los valores de la lista
courses[0] = "Ruby on Rails"
courses[1] = "MySQL"
print(courses)