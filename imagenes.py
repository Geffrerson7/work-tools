import pandas as pd
import requests
import os

# Función para descargar una imagen de una URL y guardarla en una carpeta con el nombre SKU-N
def descargar_imagenes(urls, sku, carpeta):
    urls_separadas = urls.split(',')  # Dividir las URLs por la coma
    for i, url in enumerate(urls_separadas, start=1):
        nombre_archivo = f"{sku}-{i}.jpg"  # Nombre del archivo será SKU-N
        ruta_archivo = os.path.join(carpeta, nombre_archivo)  # Construir la ruta completa del archivo
        with open(ruta_archivo, 'wb') as archivo:
            respuesta = requests.get(url.strip())  # Eliminar posibles espacios en blanco
            archivo.write(respuesta.content)

# Cargar el archivo Excel
archivo_excel = "mi_archivo.xlsx"  # Asumiendo que el archivo está en el mismo directorio que el script
df = pd.read_excel(archivo_excel)

# Carpeta donde se guardarán las imágenes
carpeta_destino = "C:/Users/geffe/Desktop/codigo/EXCEL/img-gef"
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# List to store SKUs with empty image links
skus_sin_imagen = []

# Iterar sobre las filas del DataFrame
for index, fila in df.iterrows():
    enlaces_imagen = fila['link']
    sku = fila['SKU']
    if pd.isna(enlaces_imagen) or enlaces_imagen.strip() == "":
        skus_sin_imagen.append(sku)
    else:
        descargar_imagenes(enlaces_imagen, sku, carpeta_destino)

# Guardar los SKUs sin imagen en un nuevo archivo Excel
df_sin_imagen = pd.DataFrame({'SKU': skus_sin_imagen})
df_sin_imagen.to_excel('skus_sin_imagen.xlsx', index=False)

print("¡Proceso completado!")
