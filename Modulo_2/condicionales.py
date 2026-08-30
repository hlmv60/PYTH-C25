#if condicional simple 
#caso: verificar si un numero es positivo 
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
    
#if - elif - else - condicional compuesto - múltiple
#Switch - Case 
#Caso: Clasificar calificaciones
calificacion = 95
bandera = True
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")
#Caso: Determinar el tipo de dia
dia = "Miercoles"
if dia == "Lunes":
    print("Inicio de Semana")
elif dia == "Viernes":
    print("Fin de semana laboral")
#elif dia == "Sabado" or dia == "Domingo"
elif dia in ["Sabado","Domingo"]:
    print("Fin de Semana")
else:
    print("Dia entre semana")

#Caso: Evaluación de desempeño académico
calificacion = int(input("Ingrese la calificación del estudiante: "))
asistencia = int(input("Ingrese el porsentaje de asistencia del estudiante (número): ")) #Porcentaje de asistencia
participacion = input("Ingrese la participación del estudiante (puede ser: 'alta','media','baja'): ") # alta media baja 

if (calificacion >= 90) & ( asistencia >= 95) & (participacion == "alta"):
    print("Desempeño sobresaliente")
elif calificacion >= 80 and asistencia >= 85 and participacion in ['alta','tamedia']:
    print("Desempeño bueno")
elif calificacion >= 70 and asistencia >= 75:
    print("Desempeño aceptable")
else:
    print("Desempeño insufucuente")
