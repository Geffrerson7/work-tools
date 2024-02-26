import pandas as pd

# Función para quitar "Descripion:" de una cadena
def quitar_descripcion(cadena):
    cadena = cadena.replace("Producto:", "").strip()
    cadena = cadena.replace("Producto", "").strip()
    cadena = cadena.replace("Poducto:", "").strip()
    cadena = cadena.replace("Descripción:", "").strip()
    cadena = cadena.replace("Descripción", "").strip()
    cadena = cadena.replace("Descripcion:", "").strip()
    cadena = cadena.replace("Descripcion", "").strip()

    return cadena

# Cargar el archivo Excel
archivo_excel = "mi_descripcion.xlsx"  # Asumiendo que el archivo está en el mismo directorio que el script

# Cargar el archivo Excel en un DataFrame de pandas
df = pd.read_excel(archivo_excel)

# Aplicar la función quitar_descripcion a la columna deseada
columna_deseada = 'Descripcion'  # Reemplazar 'Nombre de la columna' por el nombre de la columna deseada
df[columna_deseada] = df[columna_deseada].apply(quitar_descripcion)

# Guarda el resultado en un nuevo archivo Excel
df.to_excel('nueva_descripcion.xlsx', index=False)
