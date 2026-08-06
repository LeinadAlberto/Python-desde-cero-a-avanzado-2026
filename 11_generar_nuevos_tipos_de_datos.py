""" 
    Crear un programa que nos permita introducir mas informacion de un usuario.
"""
# int - float - str
# ==

first_name = input("Ingresa tu nombre: ") # str
age = int(input("Ingresa tu edad: ")) # int
height = float(input("Ingresa tu altura: ")) # float
status = input("Tu usuario se encuentra activo? (yes/no) ") == "yes" # bool

print(first_name)
print(age)
print(height)
print(status)

print()
print(type(first_name))
print(type(age))
print(type(height))
print(type(status))

print()
print(
    type(str(10))
)

numero_flotante = 23.45
convertir_string = str(numero_flotante)
print()
print(convertir_string)
print(type(convertir_string))
