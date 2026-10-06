"""
    -   Las Listas son objetos mutables, es decir en tiempo de ejecución nosotros
        podemos modificar sus longitudes, ya sea incrementandolas o decreciendolas.
    -   Utilizaremos un par de métodos para modificar la Lista.
    -   Métodos para añadir nuevos elementos a una Lista en tiempo de ejecución: 
            append() : Nos permite añadir un nuevo elemento al final de la lista.
            insert() : Nos permite insertar un nuevo elemento en nuestra lista. Recibe 2 argumentos, 
                       el primero argumento es un número entero que hace referencia al indice donde queremos
                       añadir el elemento y el segundo argumento es el elemento que queremos añadir a la lista.
            extend() : Nos permite extender nuestra lista a partir de otra lista.
    -   Formas para saber si un elemento se encuentra o no dentro de una Lista.
            in : Nos permite saber si un elemento se encuentra dentro una Lista, si el elemento existe nos
                 retorna un valor booleano en este caso True.
            index: Retorna el valor del indice de un elemento en el caso se encuentra en la Lista, caso contrario
                   retorna un mensaje de error indicando que el elemento no se encuentra en la Lista.
"""
#            -5         -4       -3      -2        -1
#             0          1        2       3         4
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # String (5)

""" Método Append - lista.append(elemento) """
courses.append("Ruby on Rails")
courses.append("PHP")
courses.append("Laravel")
# print(courses) # ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB', 'Ruby on Rails', 'PHP', 'Laravel']

""" Método Insert - lista.insert(indice, elemento) """
courses.insert(0, "Rust") # Añade el elemento de Texto "Rust" en la posición con indice 0 de la Lista.
# print(courses) # ['Rust', 'Python', 'Django', 'Flask', 'Ruby', 'MongoDB', 'Ruby on Rails', 'PHP', 'Laravel']
courses.insert(4, "C#") # Añade el elemento de Texto "C#" en la posición con indice 4 de la Lista.
# print(courses) # ['Rust', 'Python', 'Django', 'Flask', 'C#', 'Ruby', 'MongoDB', 'Ruby on Rails', 'PHP', 'Laravel']
courses.insert(2, "MySQL") # Añade el elemento de Texto "MySQL" en la posición con indice 2 de la Lista.
# print(courses) 
# ['Rust', 'Python', 'MySQL', 'Django', 'Flask', 'C#', 'Ruby', 'MongoDB', 'Ruby on Rails', 'PHP', 'Laravel']

""" Método Extend - lista.extend(new_list) """
# Defino una lista de nuevos cursos
new_courses = ["React", "Next"]

# Añadimos la nueva lista mediante el metodo extends a la anterior lista. 
courses.extend(new_courses)

print(courses)
# ['Rust', 'Python', 'MySQL', 'Django', 'Flask', 'C#', 'Ruby', 'MongoDB', 'Ruby on Rails', 'PHP', 
# 'Laravel', 'React', 'Next']

print(f"El tamaño de la lista es {len(courses)}") # El tamaño de la lista es 13

""" Método in - (nombreValor in nombreLista) """
print("Python" in courses) # True | El String "Python" si se encuentra en la Lista courses
print("Vue" in courses) # False | El String "Vue" no se encuentra en la Lista courses)

""" Método index - (nombreLista.index(nombreValor)) """
print(courses.index("Python")) # 1 | Retorna el valor del indice que ocupa el String "Python"
print(courses.index("Ruby")) # 6 | Retorna el valor del indice que ocupa el String "Ruby"
print(courses.index("Vue")) # ValueError: 'Vue' is not in list | Mensaje de error indicando que no se encontro el 
                            # el elemento en la Lista
