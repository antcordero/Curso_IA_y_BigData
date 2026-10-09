############################
# Operadores Aritméticos
############################

print(3 + 4)
print(3 - 4)
print(10 % 2)
print(10 % 3)
print(10 / 2)

print(10 // 2) # division entera, se hace la division y se redondea hacia abajo, la aproxima a un numero entero
print(10 // 3)

print(2 ** 3) # potencia, 2 elevado a la 3

# símbolo + con strings, se hace una concatenación de los strings
print("Hola" + " " + "Python")
# pero así concatena los strings juntos
print("Hola" + "Python")

# print("Hola" + 2) # esto da error, no se puede concatenar un string con un int, hay que hacer un casting del int a string
print("Hola" + str(2)) # esto funciona, se hace un casting del int a string

# strings con el símbolo * se repite el string n veces, solo funciona con enteros, no con floats
print("Hola " * 3) # esto imprime "HolaHolaHola"

############################
# Operadores de Comparativos
############################

print(3 > 4) # False
print(3 < 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
print(3 == 4) # False
print(3 != 4) # True
print()
# Ordenación alfabética
print("Hola" == "Hola") # True
print("Hola" != "Hola") # False
print("Hola" == "hola") # False, porque las mayúsculas y minúsculas son diferentes
print("Hola" > "Python") # True, porque la H es mayor que la P en el orden alfabético, por el unicode de los caracteres, ASCII
print("hola" > "bola") # True, porque la h es mayor que la b en el orden alfabético

############################
# Operadores Lógicos
############################

# existen 3 operadores lógicos: and, or, not
# and -> devuelve True si ambos operandos son True, de lo contrario devuelve False
# or -> devuelve True si al menos uno de los operandos es True, de lo contrario devuelve False
# not -> devuelve True si el operando es False, de lo contrario devuelve False

print(3 > 4 and 4 > 3) # False, porque el primer operando es False
print(3 > 4 or 4 > 3) # True, porque el segundo operando es True
print(not (3 > 4)) # True, porque el operando es False y le dice lo contrario de False, así que devuelve True