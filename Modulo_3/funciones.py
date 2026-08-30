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
  
#2. Generador de reportes

def generar_titulo(texto, simbolo):
    """
    Imprime un texto centrado y rodeado por un simbolo decorativo.
        :texto (str): El titulo o mensaje principal.
        :simbolo (str): El carácter que se usará para decorar.
    """
    
    #Multiplica un String que repite el carácter.
    decoracion = simbolo * 10
    print(f'{decoracion} {texto} {decoracion}')
    
#Llamada usando help() para ver nuestra documentación (docString)
help(generar_titulo)

#Llamada normal pasando argumentos
generar_titulo("ANALISIS FINAL", "*")
generar_titulo("ADVERTENCIA", "!")
    
      
      