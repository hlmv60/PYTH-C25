# Crear un programa para identificar la longitud de una palabra ingresada. La
# palabra correcta debe tener entre cuatro y ocho letras. toma en cuenta las
# siguientes consideraciones:
# ● Si la longitud de la palabra se encuentra en el rango de cuatro a ocho
# letras, se debe imprimir un mensaje que indique que la palabra es
# correcta.
# ● Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga:
# “Hacen falta letras. Solo tiene N letras” (siendo N el número de letras de
# la palabra).
# ● Si la palabra tiene más de 8 letras debe indicar un mensaje que diga:
# “Sobran letras. Tiene N letras” (siendo N el número de letras de la
# palabra).
while True:
    palabra = input("Ingrese la palabra a contar: ")
    
# Validar que la palabra solo contenga letras
    if  palabra.isalpha():
         break
    else:
        print("Error: debe ingresar una palabra intente otra vez: ")
        continue
# Obtener la longitud de la palabra con la iteracion del for
cont = 0   
for i in palabra :
    cont += 1

if cont < 4:
    print(f"Hacen falta letras solo tiene {cont} letras")
elif cont > 8:
    print(f"Sobran letras. Tiene {cont} letras.")
else:
    print(f"La Palabra es correcta tiene {cont} letras.")
    
print("-" * 50)

# ==========================================
# PARTE 2: Identificar cuadrante
# ==========================================    
# En las coordenadas, el primer dígito es el que se refiere al eje de las X y el
# segundo al eje de las Y, horizontal y vertical respectivamente.
# Ya que sabes esto, el ejercicio es el siguiente:
# Crear un programa que en base a 2 números de entrada, coordenadas,
# identifique en cuál de los 4 cuadrantes se encuentra el punto. El programa
# debe verificar que ninguna coordenada sea 0. Por ejemplo
# Ingrese X: 4
# Ingrese Y: -5
# El punto se encuentra en el cuadrante IV
# (X,Y): (+,+) => Cuad. I; (-,+) => Cuad. II; (-,-) => Cuad. III; (+,-) => Cuad. IV
while True:
    try:
        x = int(input("Ingrese X: "))
        y = int(input("Ingrese Y: "))

        if x != 0 and y != 0:
            break  # Válido: son enteros y ninguno es cero salimos del bucle
        
        print("Error: Las coordenadas no pueden ser 0. Intente de nuevo.\n")

    except ValueError:
        print("Error: Debe ingresar solo números enteros válidos (ej. -5, 3, -10). Intente de nuevo.\n")
# Evaluacion del cuadrante segun los signos de X e Y    
if x > 0 and y > 0 :
    print(f"El punto ({x},{y}) se encuentra en el cuadrante I(++).")
elif  x < 0 and  y > 0:
    print(f"El punto ({x},{y}) se encuentra en el cuadrante II(-+).")
elif x < 0 and y < 0:
    print(f"El punto ({x},{y}) se encuentra en el cuadrante III(--).")
elif x > 0  and y < 0 :
    print(f"El punto ({x},{y}) se encuentra en el cuadrante IV(+-).")