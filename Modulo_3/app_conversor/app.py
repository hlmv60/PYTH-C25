#Sistema que convierte importes entre Dólares, Euros (o tu moneda local).
import conversor
import tasas #Solo para mostrar las opcionnes disponibles

def iniciar_programa():
     print('----------CONVERSOR DE MONEDAS----------')
     print(f'Monedas disponibles: {list(tasas.TASAS.keys)}')
     
     try:
         origen = input('Moneda de origen (ej. MXN):').upper()
         destino = input('Moneda de destino (ej. USD):').upper()
         monto = float(input('Cantidad a convertir:'))
         
         resultado = conversor.realizar_conversion(monto,origen,destino)
         
         if resultado is not None:
             print(f'\nResultado: {monto} {origen} {destino}')
         else:
             print(f'\nError por favor ingresa un número válido para el monto')
     except ValueError:
        print('\nError: Por favor ingrrese un número válido para el monto.')

if __name__ == "__main__":
    iniciar_programa()
       