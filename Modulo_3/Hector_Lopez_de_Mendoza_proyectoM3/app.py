# Importar los modulos
from data_generate import obtener_df
from graficador import crear_grafica_barras

def main():
    print("---Iniciando App---")
    
    try:
        # 1. Obtener los datos del generador
        df_galton = obtener_df(num_bolas=30000, num_nivel=12)
        
        # 2. Validar que el DataFrame no esté vacío
        if not df_galton.empty:
            # 3. Pasar el DataFrame al módulo de graficación
            crear_grafica_barras(df_galton, 'Contenedor', 'Cantidad_Bolas')
        else:
            print("Error: El DataFrame está vacío.")

    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')

    print('---Fin de la ejecución---')


if __name__ == "__main__":
    main()