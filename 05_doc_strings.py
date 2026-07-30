""" 
    Cuando una cadena aparece como la primera instrucción dentro de un módulo, 
    función, clase o método, Python la guarda como documentación.
    A eso se llama docstring.

    Resumen:

Sintaxis            ¿Es comentario?         ¿Es una cadena (str)?           Uso recomendado

    # comentario        ✅ Si                   ❌ No                       Comentarios                   

    """texto"""         ❌ No                   ✅ Si                       Cadenas multilínea y docstring
    
    '''texto'''         ❌ No                   ✅ Si                       Cadenas multilínea y docstring
    
"""

def saludar():
    """Muestra un saludo en pantalla.""" 
    print("\nHola") 

saludar() # Hola

# Forma de ver el docstring
print(saludar.__doc__) # Muestra un saludo en pantalla.