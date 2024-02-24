import pandas as pd

# Cargar el archivo Excel con los datos de las dos columnas
df = pd.read_excel('mi_archivo.xlsx')

# Extraer los datos de las dos columnas y combinarlos en una sola serie
serie_combinada = pd.concat([df['Columna A'], df['Columna B']]).drop_duplicates().reset_index(drop=True)

# Crear un nuevo DataFrame con la serie combinada
df_final = pd.DataFrame(serie_combinada, columns=['Columna C'])

# Guardar el DataFrame final en un nuevo archivo Excel
df_final.to_excel('datos_combinados.xlsx', index=False)