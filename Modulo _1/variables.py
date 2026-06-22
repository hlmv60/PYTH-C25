# Variable integer
chocolate = 50

# Variable float
PI = 3.141592653589793

# Variable boolean
is_active = True

# Variable string
saludo = "Hola, mundo!"

# f string
print(f"Variables simples: {chocolate}, {PI}, {is_active}, {saludo}")

#-----------------------------------------------------------------------------------------

#Variable list
# [index 0, index 1, index 2, index 3, ...]
fruits = ["apple", 50, "cherry", [1,2,3], True]

#Variable tuple
# (value 0, value 1,)
cordinates = (10.0, 20.0)

#variable Dictionary
person = {
    #key : value,
    #key : value,
    'name' : 'Juan',
    'age' : 30,
    'city' : 'Madrid',
    'hobbies' : ['football', 'read', 'trips']   
    }

print(f'Variables complejas: {fruits}, {cordinates}, {person}')

#-----------------------------------------------------------------------------------------

#Ejempla de conversion de tipos
numero_str = "100"

#numero_str + 50 No puedes sumar/concatenar un string con un entero directamente
print(f"{numero_str}50") 

numero_int = int(numero_str) + 50 # Conversion de string a entero y sumar 50
print(numero_int) # output 150 entero

fruits_str = ['10', '20', '30'] 
print(fruits_str) # Output ['10', '20', '30'] lista de strings
# fruits_int = list(map(int, fruits_str)) # Conversion de cada elemento de la lista de strings a enteros
# print(fruits_int) # Output [10, 20, 30] lista de enteros

flotante = 25.67
entero = int(flotante) # Conversion de float a entero
print(entero) # Output 25 entero
print(round(flotante,0)) # Output 26.0 

flotante_nuevo = float(numero_str) # Conversion de entero a float
print(flotante_nuevo) # Output 100.0 float
print(entero + flotante_nuevo) # Output 125.0 suma de entero y float da como resultado un float


#Ejemplo de conversion a boleano
is_boolean = True
is_boolean_strr = str(is_boolean) # Conversion de booleano a string
print(is_boolean_strr) # Output 'True' string
is_boolean_int = int(is_boolean) # Conversion de booleano a entero
print(is_boolean_int) # Output 1 entero
flotante_bool = float(is_boolean) # Conversion de booleano a float
print(flotante_bool) # Output 1.0 float
boolean_float = bool(float) # Conversion de float a booleano
print(boolean_float) # Output True booleano

fruta = 'platano'
frruta_int = int(float(fruta)) # ValueError: invalid literal for int() with base 10: 'platano'   enta un número a entero
print(frruta_int) # Output 100.52 float

#-----------------------------------------------------------------------------------------------------------------------