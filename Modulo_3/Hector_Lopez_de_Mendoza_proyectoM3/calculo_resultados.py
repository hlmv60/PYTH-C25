# Estructura Básica del Algoritmo (Lógica)
# 	• Inicialización: Definir número de bolas, número de niveles/filas de clavos (n) y probabilidad de desvío (p=0.5).
# 	• Trayectoria:
# Para cada bola:
# 		1. Iniciar posición en x=0.
# 		2. Para cada fila de 1a n, sumar +1(derecha) si un número aleatorio es mayor a 0.5, o −1(izquierda) en caso contrario.
# 		3. Registrar el contenedor final (x) donde cae la bola.
# 	• Renderizado: Contar cuántas bolas cayeron en cada contenedor y actualizar el gráfico o pantalla.
# 
# Deberás emplear dos funciones, una para calcular los resultados de las 
# canicas y la segunda para la graficación del histograma. 

import random

def cal_res (num_bolas,num_nivel,p = 0.5): 
    """
    Calcula el contenedor final de cada bola tras atravesar los clavos.
    Retorna una lista con la posición x final de cada bola.
    :num_bolas (num): Definir el numero de bolas para el calculo
    :num_nivel (num): Numero de niveles/filas de clavos (n)
    :p (float): Probabilidad de desvío p=0.5
    """
    resultados = []
    i = 0 # Contador de las bolas 

    while i <= num_bolas:
        posicion = 0
        nivel = 0 # Contador para los niveles 
        
        while nivel < num_nivel :
            # Si el numero aleatorio es menor a p las bolas caen a la derecha
            if random.random() < p:
                posicion += 1 
            nivel +=1 
        resultados.append(posicion)
        i += 1
        
    return(resultados)