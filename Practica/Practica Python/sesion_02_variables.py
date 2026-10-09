# Variables

# nomenclatura en snake_case
mi_variable = "10"
print(mi_variable)

mi_int_variable = 20
print(mi_int_variable)

mi_float_variable = 3.14
print(mi_float_variable)

mi_boolean_variable = True
print(mi_boolean_variable)

mi_string_variable = "Hola, soy una variable de tipo string"
print(mi_string_variable)


# print con diferentes argumentos
# type es una función que devuelve el tipo de dato de la variable
# casting de str devulve el tipo de dato string
print(f"\nEl valor de mi_variable es: {mi_variable}, y su tipo es: {type(mi_variable)}")

print(f"\nEl valor de mi_int_variable es: {mi_int_variable}, y su tipo es: {type(mi_int_variable)}")
mi_int_a_str_variable = str(mi_int_variable)
print(f"El valor de mi_int_variable es: {mi_int_a_str_variable}, y su tipo es: {type(mi_int_a_str_variable)}")

# Funciones del sistema (funciones precargadas en Python), ejemplo len() -> devuelve la longitud de un string
print("La longitud de mi_string_variable es: ", len(mi_string_variable))

# pedir datos al usuario -> con input()
nombre_usuario = input("Ingrese su nombre: ")
print(f"Hola, {nombre_usuario}!")

"""
Tipado de las variables
    Python es un lenguaje de tipado dinámico, lo que significa que 
    no es necesario declarar el tipo de dato de una variable al momento de su creación.
    El tipo de dato se asigna automáticamente según el valor que se le asigne a la variable.
    Sin embargo, es posible cambiar el tipo de dato de una variable en cualquier momento, 
    simplemente asignándole un nuevo valor de un tipo diferente. 
"""

address: str = "Calle Falsa 123" # se le fuerza el tipo, sirve de ayuda para saber que tipo queremos que tenga la variable
print("\n", type(address))