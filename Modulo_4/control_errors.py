#Control de errores en una division
def dividir_seguro(a, b):
    try: #Codogo con posible error
        resultado = a/b
    except ZeroDivisionError: #control del error al dividir entre cero.
        print("Error no puedes dividir entre cero.")
        return None
    except TypeError: #control del error por tipo de datos distintos (no float: o number).
        print("Error: Ambos valores debeen ser numericos.")
        return None
    else: #se ejecuta solo si no tuvimos una excepcion
        print(f"Diviion exitosa. El resultado es {resultado}")
        return resultado
    finally: #siempre se ejecuta
        print("--- Operacion finalizada---")
        
dividir_seguro(10,2)
dividir_seguro(10,0)
dividir_seguro(10,"b")

#Acceso seguro a listas
frutas = ["Manzana", "Platano", "Naranja"]
print(f"Opciones disponibles: 0 a {len(frutas) - 1}")

try:
    indice = int(input("Selecciona el numero de la fruta: "))
    seleccion = frutas[indice]
except ValueError:
    print("Error: Debes ingressar un numero entero.")
except IndexError:
    print("Error: El numero esta fuera del rango disponible")
else:
    print(f"Has seleccionado: {seleccion}")
finally:
    print("Fin del proceso de seleccion")
