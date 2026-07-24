# if condicional simple 
# caso: verificar si un numero es positivo 
numero = int(input("Ingrese un numero: "))
if numero > 0:
    print("El numero es positivo")
    
# caso validar acceso por edad
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Acceso permitido.")
    
#if-else - Condicional compuesto - doble
#Caso: Comprobar si un numero es par o impar
numero_2 = 55
if numero_2 % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
    
# Caso: Verificar si un uusario esta activo
usuario_activo = True
if usuario_activo :
    print("Bien benido de nuevo.")
else:
    print("Por favor, inicia sesión.")