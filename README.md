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

