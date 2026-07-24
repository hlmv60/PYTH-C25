# Caso de uso While: Validar número entre 1 y 10 
# validador = False
while True:
    n = input("Introduce un número entre 1 y 10 que indique el valor de bajo stock: ")
    if not (n.isdigit()):
        print("Entrada no valida intenta de nuevo")
        continue
    else:
        n = int(n)
    # if n >= 1 or n <= 10
    if 1 <= n <= 10:
        print(f"Numero Aceptado : {n}")
        break
    else:
        print("Fuera de rango intenta de nuevo:")

    


