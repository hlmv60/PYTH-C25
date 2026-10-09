# Con el lenguaje de programación Python, usando la librería requests y
# equipando las habilidades que has adquirido en este Módulo construirás una
# Pokédex obteniendo los datos de https://pokeapi.co/
# Cuando el usuario introduzca el nombre de un Pokémon, si no existe que le
# mande un mensaje de error; si existe, que muestre una imagen y las
# estadísticas (peso, tamaño, movimientos, habilidades y tipos).
# Posteriormente, guardarás toda la información del pokémon (junto con el link
# de la imagen frontal del pokémon) en un archivo .json dentro de una carpeta
# llamada “pokedex”.
# Habiendo hecho esto, subirás el código a un repositorio en tu cuenta de GitHub
# explicando cómo lo hiciste, qué bibliotecas necesitaría otro usuario para
# ejecutar el proyecto, mostrando imágenes de muestra de algún resultado de
# búsqueda de un pokémon y describiendo qué has aprendido en este módulo.

import os
import json
import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

# Crear la carpeta pokedex si no existe
os.makedirs("pokedex", exist_ok=True)

pokemon = input("Pon un pokémon: ").strip().lower()

# 1. Definir la URL
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

# 2. Realizar la petición
response = requests.get(url)

if response.status_code != 200:
    print("Pokémon no encontrado")
    exit()

# 3. Obtener datos
datos = response.json()
nombre = datos["name"]
peso = datos["weight"]
altura = datos["height"]

# 4. Obtener imagen
url_imagen = datos.get("sprites", {}).get("front_default")
if url_imagen:
    try:
        imagen = Image.open(urlopen(url_imagen))
    except Exception:
        print("El Pokémon no tiene imagen válida")
        imagen = None
else:
    imagen = None

# Mostrar imagen si existe
if imagen is not None:
    plt.figure()
    plt.title(nombre)
    plt.imshow(imagen)
    plt.axis("off")
    plt.show()

# Mostrar datos básicos
print(f"Nombre: {nombre}")
print(f"Peso: {peso}")
print(f"Tamaño: {altura}")

# Obtener listas
movimientos = [m["move"]["name"] for m in datos.get("moves", [])]
habilidades = [h["ability"]["name"] for h in datos.get("abilities", [])]
tipos = [t["type"]["name"] for t in datos.get("types", [])]

# Mostrar movimientos
print(f"\nMovimientos de {nombre}:")
for movimiento in movimientos:
    print("-", movimiento)

# Mostrar habilidades
print(f"\nHabilidades de {nombre}:")
for habilidad in habilidades:
    print("-", habilidad)

# Mostrar tipos
print(f"\nTipos de {nombre}:")
for tipo in tipos:
    print("-", tipo)

# 5. Guardar en JSON
pokemon_data = {
    "name": nombre,
    "peso": peso,
    "altura": altura,
    "movimientos": movimientos,
    "habilidades": habilidades,
    "tipos": tipos,
    "imagen_front_default": url_imagen
}

archivo_json = os.path.join("pokedex", f"{nombre}.json")

with open(archivo_json, "w", encoding="utf-8") as archivo:
    json.dump(pokemon_data, archivo, ensure_ascii=False, indent=4)

print(f"\nArchivo JSON guardado en: {archivo_json}")

    