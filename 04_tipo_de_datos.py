# En Python tenemos 4 tipos de datos
# Strings
# Integers
# Floats
# Booleans

""" 
    Strings:
    En Python existe dos formas de crear Strings ya sea con 
    comillas dobles "" o comillas simples '' 
"""

first_name = "Mon'i'ca Andrea"
last_name = 'Chav"e"z Suarez'

print()
print(first_name) # Mon'i'ca Andrea
print(last_name) # Chav"e"z Suarez

print()
print(type(first_name)) # <class 'str'>
print(type(last_name)) # <class 'str'>

mensaje = """Él dijo: "It's fine" """

print()
print(mensaje)

""" 
    Integers:
    Los tipos de dato entero nos permite representar números enteros
    ya sea con o sin signo.
"""

age = -26

print()
print(age) # 26
print(type(age)) # <class 'int'>

numero_grande = 100_000_000 # Sintaxis que permite leer números grandes

print()
print(numero_grande) # 100000000
print(type(numero_grande)) # <class 'int'>

""" 
    Floats:
    Los tipos de dato flotante nos permite representar números con punto decimal.
    ya sea con o sin signo.
"""

pi = -3.14

print()
print(pi) # 3.14
print(type(pi)) # <class 'float'>

""" 
    Booleanos:
    En Python nos permiten representar dos tipos de valores, 
    Verdadero (True) y Falso (False) 
"""

is_active = False

print()
print(is_active) # True
print(type(is_active)) # bool