import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel('mi_archivos.xlsx')

# Contar la frecuencia de cada valor en la columna A
frecuencia_valores = df['Columna A'].value_counts()

# Filtrar los valores que se repiten más de una vez
valores_repetidos = frecuencia_valores[frecuencia_valores > 1]

# Crear un DataFrame con los valores repetidos y sus repeticiones
df_repetidos = pd.DataFrame({'Valor': valores_repetidos.index, 'Repeticiones': valores_repetidos.values})

# Guardar el DataFrame de valores repetidos en un archivo Excel
df_repetidos.to_excel('valores_repetidos.xlsx', index=False)