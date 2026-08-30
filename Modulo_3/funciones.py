#1 El calculador de envios (Scopemy globales)
#Declarar nuestra variable Global (Accesible desde cualquuier parte)

TARIFA_BASE = 50 #variable global

def calcular_envio(peso): #El peso es parametro por que lo estamos definiendo desde el nivel de la funcion
    costo = (peso * 10) + TARIFA_BASE
    return costo

precio_final = calcular_envio(10)
print(f'El costo del envio es: {precio_final}') 

#Intento de Error
#print(costo)
    