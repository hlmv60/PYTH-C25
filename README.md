#  Mi repositorio clase PYTH 25

## Fundamentos  de **Python**

Bienvenidos, a este nuevo curso de fundamentos de python.

El curso estará dividido en 4 modulos:

1. Variables, operadores y cadenas de texto
2. Estructuras de control y colecciones
3. Funciones, módulos y paquetes
4. Manejo de archivos, excepciones y consumo de APIs

# Calculadora de Índice de Masa Corporal (IMC) en Python Proyecto 1

Este es un programa desarrollado en Python que solicita al usuario sus datos personales 
(nombre, apellidos y edad) junto con sus datos de (peso en kilogramos y estatura en metros ) 
para calcular de forma precisa su Índice de Masa Corporal (IMC) 
y clasificarlo según los estándares oficiales de la Organización Mundial de la Salud (OMS).

## Características Principales

*   **Validación Manual :** El programa valida que los datos numéricos y de texto sean correctos antes de realizar cualquier operación, evitando cierres inesperados del programa.
*   **Soporte para Nombres Compuestos:** Capacidad de aceptar nombres o apellidos con espacios (ej. "María Edith" o "López de Mendoza") sin fallar en la validación alfabética.
*   **Manejo de Números Flotantes:** Validación personalizada para el peso y la estatura que admite números enteros y decimales con un único punto.
*   **Formateo Estético Automatizado:** Uso de funciones nativas de Python para corregir imperfecciones de entrada en los nombres propios.

---

## Estructura y Desarrollo del Código

El flujo del programa se diseñó siguiendo los cuatro requerimientos principales del proyecto 1:

### 1. Captura de Datos Personales
Se solicita al usuario de manera secuencial su nombre, apellido paterno, apellido materno, edad, peso y estatura a través de la consola empleando la función `input()`.

### 2. Validación de Datos (Robustez del Código)
Para asegurar que las entradas no estén vacías y correspondan al tipo de dato correcto, se implementaron los siguientes filtros manuales:
*   **Limpieza de Espacios:** Se aplicó `.strip()` en todas las entradas para eliminar espacios accidentales al inicio o al final.
*   **Filtro Alfabético:** Uso de `.replace(" ", "").isalpha()` para validar que los nombres solo contengan letras, permitiendo espacios internos para nombres compuestos.
*   **Filtro de Enteros:** Uso de `.isdigit()` en la edad combinando una validación lógica para prohibir números menores o iguales a cero.
*   **Filtro Decimal Personalizado:** Para el peso y la estatura se utilizó la lógica:
    `not peso_input.replace(".", "", 1).isdigit() or peso_input.count(".") > 1`
    Esto permite remover temporalmente el punto decimal para evaluar la cadena como dígitos puros y rechaza entradas con múltiples puntos (ej. `1.7.5`).

### 3. Cálculo del IMC y Despliegue
Se aplica la fórmula matemática estándar dividiendo el peso entre el cuadrado de la estatura:

```text
          Peso (kg)
IMC = ─────────────────
      Estatura (m) × Estatura (m)
```

El resultado final se muestra formateado elegantemente a dos decimales (`:.2f`) y los nombres se transforman de forma automática a formato de título (`.title()`).

### 4. Interpretación del Resultado
Se estructuró una cadena de condiciones (if-elif-else) evaluando únicamente los límites superiores de cada categoría de la OMS. Esto elimina los vacíos y huecos decimales en los rangos de evaluación, permitiendo clasificar correctamente valores límite (por ejemplo, un IMC de 24.97).
---

## Experiencias y Aprendizajes Obtenidos
El desarrollo de este Proyecto 1 de lógica de programación en Python me dejó los siguientes aprendizajes:

1. **Dominio de Métodos de Cadenas (`Strings`):** Se profundizó en el comportamiento de métodos como `.isalpha()`, `.isdigit()`, `.strip()` y `.title()`. Se comprendieron las limitaciones de `.isalpha()` con los espacios y de `.isdigit()` con los puntos decimales.
2. **Lógica Alternativa al Control de Excepciones:** Diseñar un sistema de validación numérico decimal de manera puramente lógica (usando `.replace()` y `.count()`) en lugar de recurrir al bloque `try/except` expandió la visión algorítmica para anticipar errores de usuario.
3. **Fronteras Numéricas en Condicionales:** Al probar el código con valores límite (como un IMC de `24.97` o `29.95`), se descubrió la importancia de no dejar "huecos" entre las condiciones (ej. evaluar `imc < 25.0` en lugar de `imc <= 24.9`), garantizando que absolutamente todos los números reales caigan en la categoría correcta.
4. **Flujo Limpio de Ejecución:** El uso estratégico de `exit()` tras detectar un error asegura que el programa no continúe procesando datos corruptos o vacíos, optimizando los recursos del sistema.

---

## Requisitos e Instalación

*   **Lenguaje:** Python 3.x
*   **Librerías:** Ninguna (Usa funciones 100% nativas)

### Ejecución
1. Abre una terminal en la ruta del archivo.
2. Ejecuta el comando:
```text
   python calculadora_imc.py
```

#   Validación y Operaciones de datos Python Proyecto 2

Este proyecto en **Python** consiste en la resolución de dos ejercicios prácticos enfocados en el control de flujo, validación estricta de entradas de usuario (`inputs`) y lógica matemática básica, validación de cadenas y análisis de coordenadas .

---

##  1. Conceptos Aprendidos

Durante el desarrollo de este proyecto se pusieron en práctica y reforzaron los siguientes conceptos de programación en Python:

* **Control de flujo con bucles `while True`:** Uso de ciclos infinitos controlados para solicitar datos repetidamente hasta que el usuario ingrese información válida.
* **Manejo de excepciones (`try / except`):** Captura del error `ValueError` para evitar que el programa se detenga interruptamente si el usuario ingresa letras o símbolos donde se esperaban números.
* **Validación de cadenas (`.isalpha()` y `len()`):** 
  * `.isalpha()` para asegurar que la entrada contenga **únicamente letras** (rechazando números y caracteres especiales).
  * `len()` para obtener directamente la cantidad de caracteres de un string de forma eficiente.
* **Condicionales y operadores lógicos (`if`, `elif`, `else`):** Estructuración de múltiples caminos de ejecución según el cumplimiento de condiciones compuestas (`and`, `>`, `<`, `!=`).
* **Lógica del plano cartesiano:** Identificación de cuadrantes basados en la combinación de signos de los ejes $X$ e $Y$.

---

##  2. ¿Cómo se Realizó el Proyecto?

El proyecto se dividió en dos partes clave:

### Parte 1: Validación y Conteo de Palabras
1. **Captura y validación de texto:**
   Se utiliza un bucle `while` junto con la función `.isalpha()` para solicitar una palabra. Si el usuario ingresa números o símbolos, el programa muestra un mensaje de error y solicita el texto de nuevo.
2. **Evaluación de la longitud:**
   Se calcula la cantidad de letras usando  el  `for cont +=1` que se puede sustituir por `len(palabra)` y se compara mediante condicionales:
   * **Menos de 4 letras:** Imprime que faltan letras e indica la cantidad actual ($N$).
   * **Más de 8 letras:** Imprime que sobran letras e indica la cantidad actual ($N$).
   * **Entre 4 y 8 letras:** Confirma que la palabra es correcta.

---

### Parte 2: Identificación de Cuadrantes Cartesianos
1. **Entrada y conversión de datos:**
   Se solicita la entrada de los ejes $X$ e $Y$. Utilizando un bloque `try / except ValueError`, se garantiza que ambos valores sean enteros válidos (admitiendo números negativos y positivos).
2. **Restricción del cero ($0$):**
   Se valida mediante la condición `if x != 0 and y != 0` que ninguno de los ejes sea igual a cero. De lo contrario, se solicita nuevamente el ingreso.
3. **Ubicación en el cuadrante:**
   Una vez validadas las coordenadas, se determina el cuadrante según la siguiente lógica de signos:
   * **Cuadrante I:** $X > 0, Y > 0 \quad (+,+)$
   * **Cuadrante II:** $X < 0, Y > 0 \quad (-,+)$
   * **Cuadrante III:** $X < 0, Y < 0 \quad (-,-)$
   * **Cuadrante IV:** $X > 0, Y < 0 \quad (+,-)$

---
## 💻 Código Fuente del Proyecto
```python
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

# ==========================================
# PARTE 2: Identificar cuadrante
# ==========================================    

while True:
    try:
        x = int(input("Ingrese X: "))
        y = int(input("Ingrese Y: "))

        if x != 0 and y != 0:
            break  # Válido: son enteros y ninguno es cero salimos del bucle
        
        print("Error: Las coordenadas no pueden ser 0. Intente de nuevo.\n")

    except ValueError:
        print("Error: Debe ingresar solo números enteros válidos (ej. -5, 3, -10). Intente de nuevo.\n")
# Evaluacion del cuadrante segun los signos de X e Y    
if x > 0 and y > 0 :
    print(f"El punto ({x},{y}) se encuentra en el cuadrante I(++).")
elif  x < 0 and  y > 0:
    print(f"El punto ({x},{y}) se encuentra en el cuadrante II(-+).")
elif x < 0 and y < 0:
    print(f"El punto ({x},{y}) se encuentra en el cuadrante III(--).")
elif x > 0  and y < 0 :
    print(f"El punto ({x},{y}) se encuentra en el cuadrante IV(+-).")
