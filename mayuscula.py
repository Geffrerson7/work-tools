import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel('mi_archivo.xlsx')

# Definir una función para capitalizar la primera letra de cada palabra en una cadena
def capitalizar_primera_letra(cadena):
    return ' '.join(word.capitalize() for word in cadena.split())

# Aplicar la función a la columna deseada
df['Columna A'] = df['Columna A'].apply(capitalizar_primera_letra)

# Guardar el DataFrame modificado en un nuevo archivo Excel
df.to_excel('nombre_mayuscula.xlsx', index=False)
