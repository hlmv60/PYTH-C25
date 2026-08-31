import pandas as pd
from calculo_resultados import cal_res

def obtener_df(num_bolas = 3000, num_nivel = 12 ):
   # 1. Obtener loos datos de la Simulacion posiciones en crudo
   posiciones = cal_res(num_bolas, num_nivel)
   
   # 2. Contar la frecuencia o cuantas bolas cayeron en los contenedores
   frecuencias = {}
   for pos in posiciones:
        if pos in frecuencias:
            frecuencias[pos] += 1
        else:
            frecuencias[pos] = 1

    # 3. Separar y ordenar las llaves (X) y los valores (Y)
   eje_x = sorted(frecuencias.keys())
   eje_y = [frecuencias[x] for x in eje_x]

    # 4. Usar zip para unir posisiones eje x contenedor con eje y cantidad de bolas / frecuencias
   datos_emparejados = list(zip(eje_x, eje_y))

    # 5. Crear el DataFrame
   df = pd.DataFrame(datos_emparejados, columns=['Contenedor', 'Cantidad_Bolas'])

   return df
   

