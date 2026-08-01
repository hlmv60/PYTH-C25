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
