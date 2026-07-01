# Pedir al usuario que ingrese sus datos personales
# Validar los datos ingresados que no estén vacíos y que sean del tipo correcto
# Calcular el IMC del usuario y mostrar los resultados al usuario
# Interpretar el resultado del IMC y mostrar un mensaje al usuario

nombre = input("Ingrese su nombre: ").strip()

if not nombre or not nombre.replace(" ", "").isalpha():
    print("Error: El nombre no puede estar vacío ni contener numeros o caracteres especiales.")
    exit()

apellidoPat = input("Ingrese su apellido paterno: ").strip()

if not apellidoPat or not apellidoPat.replace(" ", "").isalpha():
    print("Error: El apellido paterno no puede estar vacío ni contener numeros o caracteres especiales.")
    exit()
   
apellidoMat = input("Ingrese su apellido materno: ").strip()      

if not apellidoMat or not apellidoMat.replace(" ", "").isalpha():
    print("Error: El apellido materno no puede estar vacío ni contener numeros o caracteres especiales.")
    exit()

edad = input("Ingrese su edad: ").strip()

if not edad.isdigit():
    print("Error: La edad debe ser un número.")
    exit()
    
edad = int(edad)

if edad <= 0:
    print("Error: La edad debe ser un número positivo.")
    exit()

peso_input = input("Ingrese su peso en kg: ").strip()

# Validamos: quitamos un punto decimal y verificamos que el resto sean solo dígitos
# También nos aseguramos de que no esté vacío y de que no tenga más de un punto
if not peso_input or not peso_input.replace(".", "", 1).isdigit() or peso_input.count(".") > 1:
    print("Error: El peso debe ser un número entero o decimal válido (ej. 80 o 75.5).")
    exit()
    
# Si pasó la validación, la conversión a float es 100% segura
peso = float(peso_input)

if peso <= 0:
    print("Error: El peso debe ser un número positivo mayor a cero.")
    exit()
    
estatura_input = input("Ingrese su estatura en metros: ").strip()
if not estatura_input or not estatura_input.replace(".", "", 1).isdigit() or estatura_input.count(".") > 1:
    print("Error: La estatura debe ser un número entero o decimal válido (ej. 1.75).")
    exit()
    
estatura = float(estatura_input)

if estatura <= 0:
    print("Error: La estatura debe ser un número mayor a cero.")
    exit()
    
# Calcular el IMC

imc = peso / (estatura ** 2)

# Mostrar los resultados al usuario

print("\n" + "="*40)
print(f"Usuario: {nombre.title()} {apellidoPat.title()} {apellidoMat.title()}")
print(f"Edad: {edad} años")
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")