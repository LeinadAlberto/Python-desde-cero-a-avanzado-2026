- Recomendable contar con Python 3.8 o superior

- Si instalas Python en Windows recuerda añadir Python al Path

- Como abrir el Interprete Interactivo de Python (REPL)

    - En Windows escribir el comando 'python' o 'py'
    - En Linux o macOS escribir el comando 'python3'
    - Ese >>> indica que ya estás dentro del intérprete de Python 

- Qué significa REPL 
    - Describe exactamente cómo funciona el interprete de Python
        - Read (Leer) -> Python lee la instrucción que escribes
        - Eval (Evaluar) -> La interpreta y la ejecuta
        - Print (Imprimir) -> Muestra el resultado en pantalla, si lo hay.
        - Loop (Bucle) -> Espera a que escribas otra instrucción y repite el proceso.

- Como ver la versión de Python predeterminada 

    - Con el comando 'python --version'  -> en Windows
    - Con el comando 'python3 --version' -> en Linux y macOS

    - Ejemplo de salida 'Python 3.12.1'

- Como buscar la ubicación del ejecutable llamado py
    - El comando es 'where py'
    - Busca en las carpetas incluidas en la variable de entorno PATH y muestra
      dónde está el archivo py.exe

- Como salir del modo intérprete interactivo de Python
    - Con las funciones exit() o quit() 
    - Y la combinación de teclas (ctrl + z)
    - Ambas hacen que el intérprete termine y regrese a la terminal.

- ¿Qué es una convención?
    - Una convención es un conjunto de reglas o recomendaciones que la mayoria
      de los programadores acepta seguir para escribir código de manera uniforme. 
    - No son reglas obligatorias del lenguaje, sino buenas prácticas.
    - En Python existe el documento oficial llamado PEP 8(Python Enhancement Proposal 8).
      que significa (Propuesta de Mejora de Python número 8).
    - Otras convenciones de nombres
        
        Convención          Ejemplo                 Uso Común

        snake_case          precio_total            Variables, funciones y archivos en Python
        camelCase           precioTotal             Muy común en JavaScript y Java
        PascalCase          PrecioTotal             Clases en Python y otros lenguajes
        UPPER_CASE          MAX_INTENTOS            Constantes en Python