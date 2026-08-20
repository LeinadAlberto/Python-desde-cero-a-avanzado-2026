"""
    -   Las Listas son objetos mutables, es decir en tiempo de ejecución nosotros
        podemos modificar sus longitudes, ya sea incrementandolas o decreciendolas.
    -   Utilizaremos un par de métodos para modificar la Lista.
    -   Método para añadir nuevos elementos: 
            append() : Nos permite añadir un nuevo elemento al final de la lista.
            insert() : Nos permite insertar un nuevo elemento en nuestra lista. Recibe 2 argumentos, 
                       el primero argumento es un número entero que hace referencia al indice donde queremos
                       añadir el elemento y el segundo argumento es el elemento que queremos añadir a la lista.

"""
#            -5         -4       -3      -2        -1
#             0          1        2       3         4
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # String (5)

courses.append("Ruby on Rails")
courses.append("PHP")
courses.append("Laravel")
# print(courses) # ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB', 'Ruby on Rails', 'PHP', 'Laravel']

courses.insert(0, "Rust") # Añade el elemento de Texto "Rust" en la posición con indice 0 de la Lista.
print(courses) # ['Rust', 'Python', 'Django', 'Flask', 'Ruby', 'MongoDB', 'Ruby on Rails', 'PHP', 'Laravel']
courses.insert(4, "C#") # Añade el elemento de Texto "C#" en la posición con indice 4 de la Lista.
print(courses) # ['Rust', 'Python', 'Django', 'Flask', 'C#', 'Ruby', 'MongoDB', 'Ruby on Rails', 'PHP', 'Laravel']
courses.insert(2, "MySQL") # Añade el elemento de Texto "MySQL" en la posición con indice 2 de la Lista.
print(courses) 
# ['Rust', 'Python', 'MySQL', 'Django', 'Flask', 'C#', 'Ruby', 'MongoDB', 'Ruby on Rails', 'PHP', 'Laravel']

print(f"El tamaño de la lista es {len(courses)}")

