"""  
- Como definir una variable:
    <variable> = <valor>

- Como mostrar el tipo de dato de una variable
    type(nombre_variable)

- Según el estándar oficial de Python (PEP 8), 
  las variables deben seguir estas recomendaciones.

- Snake_case es una convención para escribir nombres de 
  variables, funciones y archivos donde: 
  - Todas las letras van en minúsculas.
  - Las palabras se separan con un guion bajo (_).
"""

name = "\nDaniel Canaviri"
print(name) # Daniel Canaviri
print(type(name)) # <class 'str'>

edad = 10 
print(edad) # 10
print(type(edad)) # <class 'int'>

fecha_nacimiento = "23/08/2026"
print(fecha_nacimiento) # 23/08/2026
print(type(fecha_nacimiento)) # <class 'str'>

# Definición de variables siguiendo la propuesta (PEP 484)
# Anotaciones de Tipos en Python
apellido: str = "Canaviri"
estatura: float = 1.64

print(apellido)
print(estatura)